from config import *
from psychopy import visual, core, event
import time
import random

match = ['match','opposite','meaningless']
english = ['chinese','english']

trial_settings = [(i,j) for i in match for j in english]*3
random.shuffle(trial_settings)
trial_settings = trial_settings+list(reversed(trial_settings))

def trial(win, match, english):
    # 这里未做讲解，是我闲来无聊做了一个数字的倒计时。
    countdown = visual.TextStim(win, text=u'',
                             height=0.1,
                             pos=(0.0, 0.0),
                             bold=True,
                             italic=False,
                             color='white')
    dtimer = core.CountdownTimer(3)
    while dtimer.getTime() > 0:
        countdown.text = str(int(dtimer.getTime())+1)
        countdown.draw()
        win.flip()

    seed = time.time()%1000
    generator = None
    if match=='opposite':
        generator = opposite_generator(seed,english=='english')
    elif match=='match':
        generator = match_generator(seed,english=='english')
    else:
        generator = meaningless_generator(seed,english=='english')
    result = generator.generate(12)

    if english=='english':
        for i in range(12):
            text = visual.TextStim(win, text=result[i].word,
                                   height=0.12,
                                   pos=(0.0,0.8-i*0.15),
                                   bold=True,
                                   italic=False,
                                   color=result[i].color
                                   )
            text.draw()
    else:
        for i in range(12):
            text = visual.TextStim(win, text=result[i].word,
                                   height=0.12,
                                   pos=(0.0,0.8-i*0.15),
                                   bold=True,
                                   italic=False,
                                   color=result[i].color,
                                   font='simhei'
                                   )
            text.draw()

    # 时钟
    timer = core.Clock()
    win.flip()
    timer.reset()
    event.waitKeys()
    readtime = timer.getTime()  # 获取时间
    return readtime


def random_str(slen=10):
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
    sa = []
    for i in range(slen):
      sa.append(random.choice(seed))
    return ''.join(sa)


if __name__=="__main__":
    # 创建窗口
    win = visual.Window(fullscr=True,
                        color=(-1.0, -1.0, -1.0))
    trial(win,1,1)