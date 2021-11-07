from service.systemdAnalyseService import SystemdAnalyseService

getBootTime = SystemdAnalyseService.getBootTime()
print("Boot Time = " + str(getBootTime))

getKernelCompileTime = SystemdAnalyseService.getKernelCompileTime()
print("Kernel Compile Time = " + str(getKernelCompileTime))
