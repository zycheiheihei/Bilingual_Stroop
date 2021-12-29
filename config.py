import random

class abstract_word:
    lookup = {u'蓝':(0.0,0.0,1.0),u'红':(1.0,0.0,0.0),u'绿':(0.0,1.0,0.0),u'黄':(1.0,1.0,0.0), u'灰':(0.0,0.0,0.0), u'白':(1.0,1.0,1.0)}
    dictionary = {u'蓝':'blue',u'红':'red',u'绿':'green',u'黄':'yellow', u'灰':'grey', u'白':'white',u'日':'heart',u'月':'mate',u'上':'upper',u'放':'free',u'走':'walk',u'下':'down'}
    meaningless = {u'日':'sun',u'月':'moon',u'上':'upper',u'放':'free',u'走':'walk',u'下':'down'}
    def __init__(self, w, c, english=False):
        self.word = w
        if english:
            self.word = abstract_word.dictionary[w]
        self.color = c
        self.match = False if w not in abstract_word.lookup else abstract_word.lookup[w]==c

    def output(self):
        return print(self.word,self.color,self.match)


class generator:
    def __init__(self, seed = 1, english = False):
        random.seed(seed)
        self.english=english

    def generate(self, length):
        pass

class match_generator(generator):
    def __init__(self,seed=1, english = False):
        super(match_generator,self).__init__(seed, english)

    def generate(self, length):
        samples = [random.choice(list(abstract_word.lookup.keys())) for i in range(length)]
        result = [abstract_word(w,abstract_word.lookup[w], self.english) for w in samples]
        return result

class opposite_generator(generator):
    def __init__(self,seed=1, english = False):
        super(opposite_generator, self).__init__(seed,english)

    def generate(self, length):
        samples = [random.choice(list(abstract_word.lookup.keys())) for i in range(length)]
        result = [abstract_word(w, random.sample(set(list(abstract_word.lookup.values())).difference({abstract_word.lookup[w]}), 1)[0], self.english) for w in samples]
        return result

class meaningless_generator(generator):
    def __init__(self, seed=1, english = False):
        super(meaningless_generator, self).__init__(seed, english)

    def generate(self, length):
        samples = [random.choice(list(abstract_word.meaningless.keys())) for i in range(length)]
        colors = [random.choice(list(abstract_word.lookup.values())) for i in range(length)]
        result = [abstract_word(samples[i],colors[i], self.english) for i in range(length)]
        return result

class X_generator(generator):
    def __init__(self, seed=1, english = False):
        super(X_generator, self).__init__(seed, english)

    def generate(self, length):
        colors = [random.choice(list(abstract_word.lookup.values())) for i in range(length)]
        result = [abstract_word('X',colors[i]) for i in range(length)]
        return result


if __name__=="__main__":
    gen = meaningless_generator(english=True)
    a = gen.generate(10)
    for k in a:
        k.output()

