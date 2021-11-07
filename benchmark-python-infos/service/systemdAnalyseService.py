from utils.systemdAnalyse import SystemdAnalyse
import os


class SystemdAnalyseService:
    def getBootTime():
        with os.popen('systemd-analyze') as fd:
            res = 0
            for line in fd:
                totalTime = SystemdAnalyse.systemdAnalyseRegex(line=line, res=res)
                return round(totalTime, 1)

    def getKernelCompileTime():
        with os.popen('systemd-analyze') as fd:
            res = 0
            for line in fd:
                totalTime = SystemdAnalyse.systemdAnalyseKernelRegex(line=line, res=res)
                return round(totalTime, 1)

    def getCriticalChain():
        with os.popen('systemd-analyze critical-chain') as fd:
            res = ""
            for line in fd:
                res += line
        return res

    def getSvg():
        with os.popen('systemd-analyze plot') as fd:
            res = ""
            for line in fd:
                res += line
        return res

    if __name__ == '__main__':
        print(getBootTime())
        print(getKernelCompileTime())
        # print(getCriticalChain())
        # print(getSvg())
