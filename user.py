from imports import *

procs = []

for root1, dirs, files in os.walk(dir):

    #print(dirs)

    for dir1 in dirs:

        #print(dir1)

        for root, dirs1, files in os.walk(f"{root1}/{dir1}"):

            out = open(f"{root}/runout.txt", "w")

            #print("walking", dir1)

            #print(root, dirs1, files)

            #print(files)

            if "start" in files:

                procs.append(subprocess.Popen(f"bash {root}/start".split(), stdout = out, stderr = out))

            break

    break

#for i in procs:

    #print(i.communicate())

    #i.wait()
