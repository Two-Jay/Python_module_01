
class Evaluator():
    @classmethod
    def zip_evaluate(cls, coefs, words):
        if len(coefs) != len(words):
            return -1
        ret = 0
        for word, weight in zip(words, coefs):
            ret = ret + (len(word) * weight)
        return ret
    
    @classmethod
    def enumerate_evaluate(cls, coefs, words):
        if len(coefs) != len(words):
            return -1
        ret = 0
        for i, word in enumerate(words):
            ret = ret + (len(word) * coefs[i])
        return ret
    

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(coefs, words))
print(Evaluator.enumerate_evaluate(coefs, words))
words.append("n")
print(Evaluator.zip_evaluate(coefs, words))
print(Evaluator.enumerate_evaluate(coefs, words))