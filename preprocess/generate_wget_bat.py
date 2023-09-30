import os



def generate_math_bat():
    f = open(os.path.join(os.path.abspath('..'), 'resources', 'download_math.bat'), 'w')
    for i in range(106):
        cmd = 'wget --recursive --no-parent --accept 32h-killmap-files.tar.gz http://fault-localization.cs.washington.edu/data/Math/' + str(i + 1)
        f.write(cmd + '\n')
    for i in range(106):
        cmd = 'wget --recursive --no-parent --accept 32h-unoptimized-killmap-files.tar.gz http://fault-localization.cs.washington.edu/data/Math/' + str(i + 1)
        f.write(cmd + '\n')
    for i in range(106):
        cmd = 'wget --recursive --no-parent --accept 168h-killmap-files.tar.gz http://fault-localization.cs.washington.edu/data/Math/' + str(i + 1)
        f.write(cmd + '\n')
    f.close()



def generate_chart_bat():
    f = open(os.path.join(os.path.abspath('..'), 'resources', 'download_chart.bat'), 'w')
    for i in range(26):
        cmd = 'wget --recursive --no-parent --accept 32h-killmap-files.tar.gz http://fault-localization.cs.washington.edu/data/Chart/' + str(i + 1)
        f.write(cmd + '\n')
    for i in range(26):
        cmd = 'wget --recursive --no-parent --accept 32h-unoptimized-killmap-files.tar.gz http://fault-localization.cs.washington.edu/data/Chart/' + str(i + 1)
        f.write(cmd + '\n')
    for i in range(26):
        cmd = 'wget --recursive --no-parent --accept 168h-killmap-files.tar.gz http://fault-localization.cs.washington.edu/data/Chart/' + str(i + 1)
        f.write(cmd + '\n')
    f.close()

def generate_time_bat():
    f = open(os.path.join(os.path.abspath('..'), 'resources', 'download_time.bat'), 'w')
    for i in range(27):
        cmd = 'wget --recursive --no-parent --accept 32h-killmap-files.tar.gz http://fault-localization.cs.washington.edu/data/Time/' + str(i + 1)
        f.write(cmd + '\n')
    for i in range(27):
        cmd = 'wget --recursive --no-parent --accept 32h-unoptimized-killmap-files.tar.gz http://fault-localization.cs.washington.edu/data/Time/' + str(i + 1)
        f.write(cmd + '\n')
    for i in range(27):
        cmd = 'wget --recursive --no-parent --accept 168h-killmap-files.tar.gz http://fault-localization.cs.washington.edu/data/Time/' + str(i + 1)
        f.write(cmd + '\n')
    f.close()

def generate_lang_bat():
    f = open(os.path.join(os.path.abspath('..'), 'resources', 'download_lang.bat'), 'w')
    for i in range(65):
        cmd = 'wget --recursive --no-parent --accept 32h-killmap-files.tar.gz http://fault-localization.cs.washington.edu/data/Lang/' + str(
            i + 1)
        f.write(cmd + '\n')
    for i in range(65):
        cmd = 'wget --recursive --no-parent --accept 32h-unoptimized-killmap-files.tar.gz http://fault-localization.cs.washington.edu/data/Lang/' + str(
            i + 1)
        f.write(cmd + '\n')
    for i in range(65):
        cmd = 'wget --recursive --no-parent --accept 168h-killmap-files.tar.gz http://fault-localization.cs.washington.edu/data/Lang/' + str(
            i + 1)
        f.write(cmd + '\n')
    f.close()

def generate_mockito_bat():
    f = open(os.path.join(os.path.abspath('..'), 'resources', 'download_mockito.bat'), 'w')
    for i in range(38):
        cmd = 'wget --recursive --no-parent --accept 32h-killmap-files.tar.gz http://fault-localization.cs.washington.edu/data/Mockito/' + str(
            i + 1)
        f.write(cmd + '\n')
    for i in range(38):
        cmd = 'wget --recursive --no-parent --accept 32h-unoptimized-killmap-files.tar.gz http://fault-localization.cs.washington.edu/data/Mockito/' + str(
            i + 1)
        f.write(cmd + '\n')
    for i in range(38):
        cmd = 'wget --recursive --no-parent --accept 168h-killmap-files.tar.gz http://fault-localization.cs.washington.edu/data/Mockito/' + str(
            i + 1)
        f.write(cmd + '\n')
    f.close()

def generate_closure_bat():
    f = open(os.path.join(os.path.abspath('..'), 'resources', 'download_closure.bat'), 'w')
    for i in range(133):
        cmd = 'wget --recursive --no-parent --accept 32h-killmap-files.tar.gz http://fault-localization.cs.washington.edu/data/Closure/' + str(
            i + 1)
        f.write(cmd + '\n')
    for i in range(133):
        cmd = 'wget --recursive --no-parent --accept 32h-unoptimized-killmap-files.tar.gz http://fault-localization.cs.washington.edu/data/Closure/' + str(
            i + 1)
        f.write(cmd + '\n')
    for i in range(133):
        cmd = 'wget --recursive --no-parent --accept 168h-killmap-files.tar.gz http://fault-localization.cs.washington.edu/data/Closure/' + str(
            i + 1)
        f.write(cmd + '\n')
    f.close()






if __name__ == '__main__':
    generate_math_bat()
    generate_chart_bat()
    generate_lang_bat()
    generate_time_bat()
    generate_closure_bat()
    generate_mockito_bat()

    pass
