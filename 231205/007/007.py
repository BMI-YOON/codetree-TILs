a, b, c = input().split()
class Problem:
    def __init__ (self, secret_code, meeting_point, time):
        self.s = secret_code 
        self.m = meeting_point 
        self.t = time 
problem = Problem(a, b, c)
print(f"""secret code : {problem.s}
meeting point : {problem.m}
time : {problem.t}""")