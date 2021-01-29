#!/usr/bin/env python3
# -*- coding=utf-8 -*-
'''
开心Python Django 学习交流q群：217840699


Author  : J.sky
Mail    : bosichong@qq.com

Author  : rcddup
Mail    : 410093793@qq.com

Author  : andywu1998
Mail    : 1078539713@qq.com
'''

__version__ = "1.0.0"

__all__ = [

    'getPSMstr', 'getMoreStep', 'getOne','get_time','getRandomNum'

]

import random
import time
import re

application_list = ['学校买回白色、彩色粉笔共45盒，其中彩色粉笔8盒，买回白粉笔多少盒？',
'学校原来有7个足球，又买来4个现在有多少个足球？',
'饲养组有30只公鸡，母鸡比公鸡多48只，有母鸡多少只？',
'淘气班捐了36本书，笑笑班再捐8本书就和淘气班捐了一样多，笑笑班捐了多少本书？',
'树上第一次飞走7只鸟，第二次飞走4只鸟，两次飞走多少只鸟？',
'一共有100只气球，其中红气球有15只，蓝气球有51只，黄气球有多少只？',
'学校有16只小白兔，卖了7只，现在有多少只？',
'乐乐有梨和苹果共15个，苹果有8个，梨有多少个？',
'有13个同学排队做操，阳阳前边有4个同学，后边有几个同学？',
'一本故事书，明明看了8页，还剩11页，这本书有多少页？',
'小巧想把草莓分给三个好朋友，小丁丁和小胖各分到6个，小亚得到4个，正好分完。小巧原来有几个草莓？',
'红铅笔有50支，蓝铅笔比红铅笔少8支，蓝铅笔有多少支？',
'妈妈买来一些糖，小丁丁吃了一半后，兰兰吃了剩下的一半，还剩下6粒糖，妈妈买来了几粒糖？',
'王心看故事书，看了12页，还剩7页，这本书有多少页？',
'小明有45本故事书,借给小丁丁17本.借给小亚14本,还剩几本?',
'小丁丁有42本课外书，先借给小亚6本，又向小胖借了9本，小丁丁现在有几本书？',
'小华给小方8张邮票后，两人的邮票同样多，小华原来比小方多几张邮票？',
'语文书12本,借走3本就与数学书一样多,数学书几本?',
'冬冬和玲玲共有16本书，玲玲有6本书，冬冬有几本书？',
'一辆公共汽车，到和平路下车35人，车上还剩20人，公共汽车中原有多少人?',
'明明要做14只纸船，做好了6只还要做几只？',
'公鸡有47只，小鸡有23只，小鸡比公鸡少多少只？',
'小青两次画了17个 ，第一次画了9个，第二次画了多少个？',
'方方上午写5行字，下午写的行数和上午同样多，一天写了多少行字？',
'小华家养32只白羊，黑羊比白羊少12只，养黑羊多少只？',
'六一儿童节，同学们做花，兰兰做了11朵花，其中黄花有3朵，做红花多少朵？',
'一本书有28页, 方方看了9页，还有几页没看?',
'欢欢第一次吃了8个山楂，第二次吃了7个，两次一共吃了多少个？',
'小巧做了27道口算，还剩18道没有做。小巧一共要做多少道口算？',
'停车场上有35辆车，开走8辆，又开走7辆，一共开走几辆？',
'河里有8只鸭子，游来了14只，河里现在有多少只鸭子？',
'欢欢要剪15个五角星，剪好了7个，还要剪几个？',
'草地上有8只白羊，6只黑羊，一共有多少只羊？',
'明明要写14行生字，已经写了10行，还要写多少行？',
'松鼠吃了8个松果，还剩16个，篮子里原来有多少个松果？',
'小明付了50元买了一本书，营业员阿姨找回他35元，这本书要几元？',
'从树上飞走8只鸟，又飞走9只，两次飞走多少只？',
'商店里有65台电视机,卖掉一些后，还剩35台电视机。卖掉多少台？',
'有两层书架，第一层有16本书，第二层比第一层多8 本，第二层有多少本？',
'小华做了35朵花, 送给幼儿园8朵, 他还有几朵?',
'小强家有10个苹果，吃了7个，还有多少个？',
'停车场上有35辆车，开走8辆，又开走7辆，一共开走几辆？',
'停车场两次开走了12辆车，第一次开走了6辆，第二次开走了多少辆？',
'爸爸买来苹果和梨共12个，共中苹果有7个，梨有几个？',
'学校体育室有6个足球 ，又买来20个，现在有多少个？',
'明明上午算了12道数学题，下午算了8道，上午比下午多算多少道题？',
'小亚要做60道口算题，还剩18题没有完成，小亚已经做完几题？',
'小明第一天写了8个大字，第二天写了10个大字，两天一共写了多少个大字？',
'饲养员养了25只白兔，又养8只黑兔，共养兔多少只？',
'盒子里的皮球取出9个, 还剩7个, 盒子里原来有几个皮球?',
'云云有9个纸鹤，又做了4个，现在有多少个？',
'一条马路两旁各种上48棵树，一共种树多少棵？',
'小红已经看了一本书的35页，还有5页没有看，这本书一共有多少页？',
'一双球鞋的价格是72元，一双布鞋的价格比一双球鞋的价格便宜了48元。一双布鞋的价格是多少元？',
'一支圆珠笔3元5角，一个橡皮擦1元，我有5元钱够不够？',
'一年级有56人参加游园比赛。在第一轮比赛中，有28人输了，又有37人参加第二轮比赛。现在有多少人参加游园比赛？',
'水果店上午卖出桔子36箱,下午卖出27,一天共卖出多少箱?',
'停车场先开走15辆车，又开走9辆车，一共开走几辆车？',
'两种树一共有多少棵？',
'一辆客车上有48个座位，上来30名乘客。还剩几个空位？',
'活动课上有26名同学参加体育活动，40名同学参加文艺活动。参加这两种活动的共有多少人？',
'我和红红都做了6朵红花，我们俩一共做了多少朵红花？',
'一年级有98个同学去旅游。第一辆车只能坐40人，第二辆车能坐55人。还有多少人不能上车？',
'少先队员学雷锋，一班和二班共做好事39件，其中一班做20件，二班做多少件?',
'河里有80只鸭子，第一次游走27只，第二只游走30只，两次共游走多少只？',
'我们班有46人，男生有20人，女生有多少人？',
'力力昨天吃了5个苹果，今天又吃了4个苹果，两天一共吃了几个苹果？',
'学校要把12箱文具送给山区小学，已送去7箱，还要送几箱？',
'李爷爷养黑兔和白兔15只。白兔有9只，黑兔有多少只？',
'书店有100本书，上午卖出45本书，下午卖出27本，一天共卖出多少本？',
'树上有10只鸟，飞走了7只还剩下多少只鸟？',
'小班再有几辆 就和中班一样多？',
'图书室里有20个女同学，有10个男同学，男同学比女同学少多少个？',
'大生有23个气球, 里面有8个红气球, 其余的是黄气球, 黄气球有多少个?',
'同学们排队做操，小明前面有4个人，后面有4个人，这一队一共有多少人？',
'商店有15把扇，卖去5把，现在有多少把？',
'盘子里共有10个苹果，小红吃了4个，还剩多少个？',
'飞走12只鸟，飞来9只鸟，树上原来有18只鸟，现在有几只鸟？',
'学校原有5瓶胶水，又买回9瓶，现在有多少瓶？',
'有9只兔子在吃胡萝卜，又来了3只兔子，一共有多少只兔子？',
'一本书有42页，小华看了一些后还剩30页没看。小华看了多少页？',
'小巧想把草莓分给三个好朋友，小丁丁和小胖各分到6个，小亚得到4个，正好分完。小巧原来有几个草莓？',
'林林已经写好30个生字，还有4个生字没写，他要写多少个生字?',
'有10头牛，走了8头，还剩多少头？',
'上衣：50元 裤子：30元 鞋：19元小华想买一件上衣、一条裤子和一双鞋，带100元，够吗？',
'山上有7只羊吃草，又来了5只，一共有多少只？',
'停车场开走58辆汽车，还剩16辆，原来有多少辆？',
'小鹿的身高是65厘米，大象比小鹿高14厘米。大象的身高是多少厘米？',
'同学们去春游，第一辆车可以坐26人，第二辆车可以坐39人，一共有80名同学，还有多少人不能上车？',
'学校有兰花和菊花共15盆，兰花有6盆，菊花有几盆？',
'小强想买一个玩具车 ，他有20元钱，还差5元才能买到，一个玩具车要多少钱？',
'蓝蓝、玲玲、小胖每人做了15朵红花，他们一共做了几朵红花？',
'学校有10个足球，16个篮球，足球比篮球少多少个？',
'明明两天看了16页书，第一天看了9页，第二天看了多少页？',
'红黄白100只气球，其中红气球20只，黄气球50只，白气球有几只',
'明明和红红一共做了11个灯笼，明明做了6个，红红做了多少个？',
'云云要写10个字，写好了6个，还要写几个？',
'轿车有23辆，卡车有37辆，大客车有18辆，一共有多少辆车？',
'花园里有兰花40盆，菊花60盆，兰花再种多少盆就和菊花同样多？?',
'桌子上有10西瓜，小明第一次吃了2块，第二次吃了2块，一共吃了多少块？']



def f1(s):
    '''
    搜索题中括号算式
    Author  : J.sky
    Mail    : bosichong@qq.com
    :param s: 算式
    :return:搜索括号算式
    '''
    ss = re.search("\(\d+[\+\-\*/\d]+\)", s)
    if ss:
        return ss.group(0)


def f2(s):
    '''
    搜索题中乘除法算式
    Author  : J.sky
    Mail    : bosichong@qq.com
    :param s: 算式
    :return: 乘除法算式
    '''
    ss = re.search("\d+[\*/]\d+", s)
    if ss:
        return ss.group(0)


def f3(s):
    '''
    搜索加减法算式
    Author  : J.sky
    Mail    : bosichong@qq.com
    :param s: 算式
    :return:加减法算式
    '''
    ss = re.search("\d+[\+\-]\d+", s)
    if ss:
        return ss.group(0)


def f4(s):
    '''
    搜索加减法乘除算式
    Author  : J.sky
    Mail    : bosichong@qq.com
    :param s: 算式
    :return: str 加减乘除算式
    '''
    ss = re.search("\d+[\+\-\*/\d]+", s)
    if ss:
        return ss.group(0)


def validator(s, result, carry, abdication):
    '''
    算式分解校验器
    Author  : J.sky
    Mail    : bosichong@qq.com
    :param s: 算式
    :return: bool
    '''

    if isResultOk(s, result):
        if f1(s):

            s = validator1(s, result, carry, abdication)

            if s:
                return validator2(s, result, carry, abdication)
            else:
                return False

        else:#校验无括号算式
            return validator2(s, result, carry, abdication)
    else:
        return False


def validator1(s, result, carry, abdication):
    '''
    算式分解校验器提取括号内算式，然后递归给validator2进行算式验证
    本方法可以递归提取括号嵌套算式
    Author  : J.sky
    Mail    : bosichong@qq.com
    :param s: 算式
    :return: bool
    '''
    while f1(s):
        fa = f1(s)
        fb = f4(f1(s))
        r = validator2(fb, result, carry, abdication)
        if r:
            s = s.replace(fa, "{}".format(int(float(r))))
        else:
            return False
    return s


def validator2(s, result, carry, abdication):
    '''
    分解乘除加减法计算结果并校验
        Author  : J.sky
    Mail    : bosichong@qq.com
    :param s:
    :return:
    '''

    # 乘除法验证
    while f2(s):
        f = f2(s)
        if isMultDivOk(f, result):
            r = eval(f)
            s = s.replace(f, str(int(float(r))))
            # print(r,s)
        else:
            return False
    # 加减法验证
    while f3(s):
        f = f3(s)
        # print(f)
        if isAddSub(f, result, carry, abdication):
            r = eval(f)
            s = s.replace(f, str(r))
        else:
            return False

    return s


def isResultOk(str, result):
    '''


    验证算式结果是否正确

    Author  : J.sky
    Mail    : bosichong@qq.com



    :param str: 一道算式题
    :param list 结果范围
    :return: bool
    '''
    try:
        # print('比较结果：',str)
        return result[0] <= eval(str) <= result[1]
    except(ZeroDivisionError):
        return False



def isMultDivOk(s, result):
    '''
    判断乘除法正确性
    :param str: 算式
    :param result list 结果范围
    :return: bool
    '''
    if re.search("/", s):
        divs = re.split("/", s)
        if int(divs[1]) == 0:
            return False
        else:
            if isResultOk(s, result) and ((int(divs[0]) % int(divs[1])) == 0) and eval(s) > 0 : # 除法，除数不能为0，并且结果在范围内,并且整除无余数
                return True
            else:
                return False
    if re.search("\*", s):
        return isResultOk(s, result)  # 乘法结果在范围内


def isAddSub(s, result, carry, abdication):
    '''
    判断加减法正确性
    :param s: str 算式
    :param result: list 结果范围
    :param carry: int 1，2，3 随机 进位 不进位
    :param abdication: int 1，2，3 随机，退位，不退位
    :return: bool
    '''
    tmp = re.split("[\+\-]", s)
    if isResultOk(s, result):
        if re.search("\+", s):

            if carry == 1:
                return True
            elif carry == 2:
                return is_addcarry(int(tmp[0]), int(tmp[1]))
            elif carry == 3:
                # print("加法进位校验")
                return is_addnocarry(int(tmp[0]), int(tmp[1]))

        elif re.search("\-", s):
            # print("减法校验开始")
            if abdication == 1:
                return True
            elif abdication == 2:
                return is_abdication(int(tmp[0]), int(tmp[1]))
            elif abdication == 3:
                return is_noabdication(int(tmp[0]), int(tmp[1]))
        else:
            return False


def getOne(formulas, signum, result, carry, abdication, is_result):
    '''
    Author  : J.sky
    Mail    : bosichong@qq.com
    根据条件生成一道一步算式题
    :param formulas: 给定的单步加法的两个值
    :param signum int 加减乘除
    :param result list 结果范围
    :param carry: int 加法进位
    :param is_result: 求结果或求运算项
    :return: bool or str 成功返回一个符合条件的加法算数题str，失败返回False
    '''
    return getMoreStep(formulas, result, [[signum], ], 1, carry, abdication, 0, is_result)


def getMoreStep(formulas, result, symbols, step, carry, abdication, is_bracket, is_result, ):
    '''


    Author  : J.sky
    Mail    : bosichong@qq.com

    :param formulas: list 整数算数项
    :param result: list 最终结果范围
    :param symbols: list 每步题的算数符号（例 [[1,2],[1,]]  第一个运算符可以为+或-，第二个运算符只能为+）
    :param step int 步数
    :param carry: int 加法是否进位
    :param abdication: int 减法是否退位
    :param is_bracket: int 是否包含括号
    :param is_result: int 求结果，求运算项
    :return: str 一道符合规则的口算运算题
    '''
    f1 = getRandomNum(formulas, step)
    f2 = getRandomNum(formulas, step)
    str1 = getPSMstr(f1, symbols, step, is_bracket)
    str2 = getPSMstr(f2, symbols, step, is_bracket)
    # print(str)
    if is_result != 3:
        if validator(str1, result, carry, abdication) and validator(str2, result, carry, abdication):
            return getXStepstr(str1, str2, is_result)

        else:
            # print("校验失败")
            return False
    else:
        ## 随机抽取应用题
        app_num = len(application_list)
        index = random.randint(0, app_num-1)
        return application_list[index]

def getPSMstr(formulas, symbols, step, is_bracket):
    '''
    Author  : J.sky
    Mail    : bosichong@qq.com
    生成算式题
    :param formulas: list 给定的算数项列表
    :param symbols: list 每步题的算数符号（例 [[1,2],[1,]]  第一个运算符可以为+或-，第二个运算符只能为+）
    :param step: int 步数
    :param is_bracket: int  括号
    :return:
    '''
    ss = ""
    sym = getRandomSymbols(symbols, step)
    for i in range(step):
        formulas.insert(i * 2 + 1, getSymbol(sym[i]))

    if is_bracket:
        k = getRandomBracket(step)  # 获得一个括号起始指针
        for i in range(2):

            if i == 0:
                formulas.insert(k + 4 * i, ('('))
            else:
                formulas.insert(k + 4 * i, (')'))

    for s in formulas:
        ss = ss + str(s)
    return ss


def getRandomBracket(step):
    '''
        Author  : J.sky
    Mail    : bosichong@qq.com
    返回一个括号起始随机数
    :param step:
    :return:
    '''
    while True:
        k = random.randint(0, step * 2 + 1 - 3)  # 获得一个括号起始指针
        if not k % 2:
            return k


########2步算式相关判断设置##########


def getXStepstr(src1, src2, is_result):
    '''
    Author  : J.sky
    Mail    : bosichong@qq.com
    给定一组算式和其结果，根据条件生成求结果或是求算数项的题型
    :param src: str 算式
    :param is_result: 0or1
    :return: str
    '''
    if is_result == 0:
        return repSymStr(src1) + "="
    elif is_result == 1:
        return getRandomItem(repSymStr(src1) + "=" + str(int(eval(src1))))
    elif is_result == 2:
        return repSymStr(src1) + "〇" + repSymStr(src2)
    else:
        raise Exception("is_result求结果，求算数项参数设置错误！")


def repSymStr(s):
    '''
        Author  : J.sky
    Mail    : bosichong@qq.com
    更换乘除法符号
    :param s:
    :return:
    '''
    if re.search('\*', s):
        s = re.sub('\*', '×', s)
    if re.search('/', s):
        s = re.sub('/', '÷', s)
    return s


def getRandomItem(sr):
    '''
    Author  : J.sky
    Mail    : bosichong@qq.com
    把得到的算式转变成求算数项口算题
    :param str: 一道算数题
    :return: str
    '''
    # print(sr)
    p = re.compile('\d+')
    sc = p.findall(sr)
    i = random.randint(0, len(sc) - 2)  # -2防止替换结果
    sr = sr.replace(sc[i], "(  )", 1)
    # print(sr)
    return sr


def getSymbol(sym):
    '''
    Author  : J.sky
    Mail    : bosichong@qq.com
    获得运算符号，用来运算结果
    :param sym: int
    :return: str
    '''
    if sym == 1:
        return "+"
    elif sym == 2:
        return "-"
    elif sym == 3:
        return "*"
    elif sym == 4:
        return "/"


def getRandomSymbols(symbols, step):
    '''

    Author  : J.sky
    Mail    : bosichong@qq.com

    返回一组运算符号

    :param symbols: list 每步题的算数符号（例 [[1,2],[1,]]  第一个运算符可以为+或-，第二个运算符只能为+）
    :param step: int 运算步
    :return:
    '''
    newList = []
    for i in range(step):
        index = random.randint(0, len(symbols[i]) - 1)
        newList.append(symbols[i][index])
    return newList


########加法相关判断设置##########


def is_addcarry(a, b, ):
    '''
    判断加法进位
    :param a: int
    :param b: int
    :param signum: str
    :return: boolean
    '''

    return (get_num(a) + get_num(b) > 10)


def is_addnocarry(a, b):
    '''
    判断加法无进位
    :param a: int
    :param b: int
    :param signum: str
    :return: boolean
    '''
    return not is_addcarry(a, b)


########减法相关判断设置##########


def is_abdication(a, b):
    '''
    判断减法退位
    :param a: int
    :param b: int
    :param signum: str
    :return: boolean
    '''

    if (get_num(a) < get_num(b)):
        return True
    else:
        return False


def is_noabdication(a, b):
    '''
    判断减法无退位
    :param a: int
    :param b: int
    :param signum: str
    :return: boolean
    '''
    return not is_abdication(a, b)


########乘法相关判断设置##########


def is_multcarry(a, b):
    '''
    判断乘法和乘法是否存在进位
    :param a: int
    :param b: int
    :param signum: str
    :return: boolean
    '''

    if (get_num(a) * get_num(b) < 10):
        return False
    else:
        return True


########除法相关判断设置##########


########其它相关判断设置##########


def is_int(num):
    '''
    判断一个数是否为整数
    :param num: int
    :return: boolean
    '''
    return isinstance(num, int)


def get_num(number):
    '''
    反回一个整数的个位数
    :param number: int
    :return: int
    '''
    value0 = number / 10
    value0 = int(value0)
    return number - value0 * 10


def getRandomNum(list, step):
    '''
    根据所给的数值范围，步数，返回合法的数值。
    Author  : andywu1998
    Mail    : 1078539713@qq.com

    Author  : J.sky
    Mail    : bosichong@qq.com
    :param list:
    :param step:
    :return:
    '''
    newList = []
    for i in range(0, step + 1):
        newList.append(random.randint(list[i][0], list[i][1]))

    return newList


# def get_timert(func):
#     '''定义一个程序运行时间计算装饰器有返回结果'''
#     def wrapper(*args, **kwargs):
#         start = time.time()#起始时间
#         res = func(*args, **kwargs)#要执行的函数
#         end = time.time()#结束时间
#         print('程序运行时间:{:.2f}ms'.format((end-start)*1000))
#         return res
#     return wrapper

def get_time(func):
    '''定义一个程序运行时间计算装饰器无返回结果'''

    def wrapper(*args, **kwargs):
        start = time.time()  # 起始时间
        func(*args, **kwargs)  # 要执行的函数
        end = time.time()  # 结束时间
        print('程序运行时间:{:.2f}ms'.format((end - start) * 1000))
        return func

    return wrapper


def main():
    # 加法进退位随机
    # print(getOne([[1, 9], [1, 9]], 1, [1, 20], 1, 1, 0))
    # print(getOne([[0, 9], [0, 9]], 2, [1, 20], 2, 2, 0))
    # print(getOne([[1, 9], [1, 9]], 3, [1, 81], 3, 1, 0))
    # print(getOne([[9, 81], [2, 9]], 4, [2, 9], 1, 1, 0))

    # 生成算式测试
    # print(getPSMstr([5,8,9,9,8],[[1,2],[1,],[2],[1,]],4,1))

    print(getMoreStep([[1, 55], [1, 99], [1, 99], [1, 9]], [1, 99], [[1, 3], [4], [4]], 2, 1, 1, 1, 0))

    # print(isMultDivOk('18/9',[1,99]))


if __name__ == '__main__':
    main()
