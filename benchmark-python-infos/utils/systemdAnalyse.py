class SystemdAnalyse():
    def systemdAnalyseRegex(line, res):
        res = res
        res = line.split("=")[1]
        res = res.split("s")[0]
        buf = res.split("min")
        if len(buf) >= 2:
            totalTime = float(buf[0])*60+float(buf[1])
            return totalTime
        else:
            totalTime = float(buf[0])
            return totalTime

    def systemdAnalyseKernelRegex(line, res):
        res = res
        res = line.split("+")[2]
        res = res.split("s")[0]
        buf = res.split("min")
        if len(buf) >= 2:
            totalTime = float(buf[0])*60+float(buf[1])
            return totalTime
        else:
            totalTime = float(buf[0])
            return totalTime
