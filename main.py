#载入所需要的库
from psychopy import visual, core, event
from trial import *
import os
import json
import numpy as np


subject = random_str(10)
print(subject)

#创建窗口
win = visual.Window(fullscr = False,
                    size=(1440,810),
                    color = (-1.0,-1.0,-1.0))

# 实验指导
#
instruction = visual.TextStim(win, text = u'欢迎您参与本课程实验，请仔细阅读下列说明。\n在此次实验过程中，您将会进行若干个试次的实验。\n在每一个试次中，您将会看到自上而下排列12个中文或英文字词。\n请尽快读出每个词的颜色（唱色任务），并在读完时按任意键。\n每个试次前会有3s倒计时。',
                         alignText='left',
                               height = 0.1,
                               pos = (-0.4,0.3),
                               bold = True,
                               italic = False,
                               color = 'white')
press_instr = visual.TextStim(win, text = u'如已清楚实验要求，请按任意键继续',
                               height = 0.1,
                               pos = (0.0,-0.2),
                               bold = True,
                               italic = False,
                               color = 'pink')

instruction.draw()
press_instr.draw()
win.flip()
event.waitKeys()
# 熟悉
warm_up = visual.TextStim(win, text = u'热身',
                               height = 0.12,
                               pos = (0.0,0.0),
                               bold = True,
                               italic = False,
                               color = 'white')
press_instr = visual.TextStim(win, text = u'请按任意键继续',
                               height = 0.1,
                               pos = (0.0,-0.2),
                               bold = True,
                               italic = False,
                               color = 'pink')

warm_up.draw()
press_instr.draw()
win.flip()
event.waitKeys()

warm_up_time = trial(win, 'meaningless', 'chinese')
warm_up_result = visual.TextStim(win, text = u'用时（s）：'+str(round(warm_up_time,3)),
                               height = 0.12,
                               pos = (0.0,0.0),
                               bold = True,
                               italic = False,
                               color = 'white')
warm_up_result.draw()
win.flip()
core.wait(1)

warm_up_time = trial(win, 'meaningless', 'english')
warm_up_result = visual.TextStim(win, text = u'用时（s）：'+str(round(warm_up_time,3)),
                               height = 0.12,
                               pos = (0.0,0.0),
                               bold = True,
                               italic = False,
                               color = 'white')
warm_up_result.draw()
win.flip()
core.wait(1)


summary = {}
for s in english:
    summary[s]={}
    for t in match:
        summary[s][t]=[]

# 正式开始
warm_up = visual.TextStim(win, text = u'实验正式开始\n每个试次后将不会呈现时间',
                               height = 0.12,
                               pos = (0.0,0.0),
                               bold = True,
                               italic = False,
                               color = 'white')
press_instr = visual.TextStim(win, text = u'请按任意键继续',
                               height = 0.1,
                               pos = (0.0,-0.2),
                               bold = True,
                               italic = False,
                               color = 'pink')

warm_up.draw()
press_instr.draw()
win.flip()
event.waitKeys()

for i in range(24):
    setting = trial_settings[i]
    result_time = trial(win,setting[0], setting[1])
    summary[setting[1]][setting[0]].append(result_time)
    # break


# 保存结果

save_text = visual.TextStim(win, text = u'保存数据中...',
                               height = 0.12,
                               pos = (0.0,0.0),
                               bold = True,
                               italic = False,
                               color = 'white')
save_text.draw()
win.flip()
core.wait(0)

if not os.path.exists('result'):
    os.mkdir('result')

with open('result/{}_raw.json'.format(subject),'w') as f:
    json.dump(summary,f)

for s in english:
    for t in match:
        data = np.array(summary[s][t])
        arithmeticMean = data.mean()
        standardDeviation = data.std()
        residualError = abs(data - arithmeticMean)
        sum = 0
        cnt = 0
        for i in range(data.shape[0]):
            if residualError[i]<3*standardDeviation:
                sum+=data[i]
                cnt+=1
            else:
                print("extreme case erased")
        summary[s][t] = round(sum/cnt,6)



if not os.path.exists('result'):
    os.mkdir('result')

with open('result/{}_avg.json'.format(subject),'w') as f:
    json.dump(summary,f)

# 保存结果

end_text = visual.TextStim(win, text = u'实验到此结束，感谢参与！',
                               height = 0.12,
                               pos = (0.0,0.0),
                               bold = True,
                               italic = False,
                               color = 'white')
end_text.draw()
win.flip()
core.wait(1)

win.close()
core.quit()