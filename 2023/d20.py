from math import prod

with open('input.txt','r') as file:
    inp = file.readlines()
    
class flip_flop:
    def __init__(self, name):
        self.name = name
        self.state = 'off'
        self.lowsigcount = 0
        self.highsigcount = 0
        
    def process(self, input, *args):
        if input == 0:
            if self.state =='off':
                self.state = 'on'
                self.highsigcount += 1
                return 1
            else:
                self.state = 'off'
                self.lowsigcount += 1
                return 0
    
    def get_sig_count(self):
        return self.lowsigcount + self.highsigcount
     
    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}: {self.name}>'                 
                
class conjunction:
    def __init__(self, name):
        self.name = name
        self.mem = dict()
        self.lowsigcount = 0
        self.highsigcount = 0
         
    def process(self, input, input_name):
        self.mem[input_name] = input
        if all(self.mem.values()):
            self.lowsigcount += 1
            return 0
        else:
            self.highsigcount += 1
            return 1
    
    def get_sig_count(self):
        return self.lowsigcount + self.highsigcount
    
    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}: {self.name},{self.mem}>'                 
    
        
class broadcast:
    def __init__(self, name, mods):
        self.name = name
        self.mods = mods
        self.lowsigcount = 0
        self.highsigcount = 0
        
    def process(self, input, *args):
        if input:
            self.highsigcount += 1
        else:
            self.lowsigcount += 1
            
        return input
    
    def get_sig_count(self):
        return self.lowsigcount + self.highsigcount
    
    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}: {self.name}>'                 
    
def initial(configs):
    all_mods = {}
    all_configs = {}
    for config in configs:
        config = config.strip()
        l, r = config.split('->')
        r = [a.strip() for a in r.strip().split(',')]
        l = l.strip()
        if '%' in l:
            l = l[1:]
            all_mods[l] = flip_flop(l)
            all_configs[l] = r
        elif '&' in l:
            l = l[1:]
            all_mods[l] = conjunction(l)
            all_configs[l] = r
        else:
            all_mods[l] = broadcast(l, r)
            all_configs[l] = r
            
    for config in configs:
        for name, conj in all_mods.items():
            if isinstance(conj, conjunction):
                config = config.strip()
                l, r = config.split('->')
                if name in r:
                    if '%' in l or '&' in l:
                        l = l.strip()[1:]
                        conj.mem[l] = 0
    print(all_mods)
    return all_configs, all_mods
    
def run(configs, all_mods, buttons):
    signal_count = 0
    for i in range(1,buttons+1):
        q = [('broadcaster', 0, 'button')] # (name, signal)
        # signal_count = i
        while q:
            mod_name, input_sig, rec_from = q.pop(0)
            for mod in configs[mod_name]:
                # PROBLEM: increasing the signal count should happen for each r side of 
                # config. this process not correct because its like l side is given 
                # another time a signal so flip flop change its state
                out_sig = all_mods[mod_name].process(input_sig, rec_from)
                if out_sig != None and mod in all_mods:
                    signal_count += 1
                    q.append((all_mods[mod].name, out_sig, mod_name))
            # print(q)       
    # return signal_count + sum([m.get_sig_count() for m in all_mods.values()])
    sum_highsigs = sum([m.highsigcount for m in all_mods.values()])
    sum_lowsigs = sum([m.lowsigcount for m in all_mods.values()])
    print(sum_lowsigs, sum_highsigs, signal_count)
    return (signal_count + sum_lowsigs)*sum_highsigs
                
                
print(run(*initial(inp),1000))