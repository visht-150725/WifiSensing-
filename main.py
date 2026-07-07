
"""
WiFiSense V1 Prototype
Requires:
pip install matplotlib numpy

Note:
Uses Windows `netsh` to read RSSI. Windows limits update precision.
"""

import subprocess,re,time,csv
from collections import deque
import numpy as np
import matplotlib.pyplot as plt

INTERVAL=0.2
WINDOW=150

tq=deque(maxlen=WINDOW)
sq=deque(maxlen=WINDOW)
events=[]

plt.style.use("dark_background")
plt.ion()
fig,ax=plt.subplots(figsize=(12,6))

start=time.time()

with open("wifi_log.csv","w",newline="") as f:
    wr=csv.writer(f)
    wr.writerow(["time","signal"])

    while True:
        try:
            out=subprocess.check_output("netsh wlan show interfaces",shell=True,text=True)
            m=re.search(r"Signal\s*:\s*(\d+)%",out)
            if not m:
                time.sleep(INTERVAL)
                continue

            sig=float(m.group(1))
            now=time.time()-start

            tq.append(now)
            sq.append(sig)
            wr.writerow([round(now,3),sig])
            f.flush()

            y=np.array(sq)

            avg=y.mean()
            std=y.std() if len(y)>1 else 0
            delta=0 if len(y)<2 else y[-1]-y[-2]

            # Exponential moving average
            alpha=0.15
            ema=[y[0]]
            for v in y[1:]:
                ema.append(alpha*v+(1-alpha)*ema[-1])
            ema=np.array(ema)

            # Motion index (derived metric, NOT AI confidence)
            motion=min(100,(abs(delta)*40)+(std*20))

            stability=max(0,100-motion)

            status="STABLE"
            if motion>60:
                status="HIGH DISTURBANCE"
            elif motion>30:
                status="MEDIUM DISTURBANCE"

            if motion>60:
                if len(events)==0 or now-events[-1][0]>3:
                    events.append((now,status))

            ymin=float(y.min())-1
            ymax=float(y.max())+1
            if ymax-ymin<2:
                ymin-=1
                ymax+=1

            ax.clear()
            ax.plot(tq,y,color="#00d9ff",lw=2,label="RSSI")
            ax.plot(tq,ema,color="orange",lw=2,label="EMA")

            ax.set_ylim(ymin,ymax)
            ax.set_xlim(max(0,now-30),max(30,now))
            ax.grid(alpha=.25)

            info=f"""
WiFiSense V1

Current RSSI : {sig:.0f} %
Average      : {avg:.2f} %
EMA          : {ema[-1]:.2f} %
Std Dev      : {std:.3f}
ΔRSSI        : {delta:+.2f}
Motion Index : {motion:.1f}/100
Stability    : {stability:.1f} %
Status       : {status}
Samples      : {len(y)}
Runtime      : {int(now)} sec
"""

            ax.text(.01,.98,info,
                    transform=ax.transAxes,
                    va="top",
                    family="monospace",
                    fontsize=10,
                    bbox=dict(facecolor="#202020",alpha=.9))

            if events:
                txt="\n".join(
                    f"{int(t)}s : {s}" for t,s in events[-5:]
                )
                ax.text(.75,.98,
                        "Recent Events\n\n"+txt,
                        transform=ax.transAxes,
                        va="top",
                        fontsize=9,
                        bbox=dict(facecolor="#202020",alpha=.9))

            ax.set_title("WiFiSense V1 Prototype")
            ax.set_xlabel("Time (seconds)")
            ax.set_ylabel("RSSI (%)")
            ax.legend()

            plt.tight_layout()
            plt.pause(.001)

            time.sleep(INTERVAL)

        except KeyboardInterrupt:
            break
