class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ls = "".join(v.upper() for v in s.split("-"))
        ns = []
        
        if len(ls)%k == 0:
            for i in range(len(ls)//k):
                ns.append(ls[i*k:(i+1)*k])
        else:
            l = len(ls)%k
            ns.append(ls[0:l])
            ls = ls[l:]
            
            for i in range(len(ls)//k):
                ns.append(ls[i*k:(i+1)*k])
                
        return "-".join(s for s in ns)