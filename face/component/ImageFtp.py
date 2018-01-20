import time
from ftplib import FTP, error_temp


class ImageUpload:
    def __init__(self, hostname, username, password, remoteDir):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.remoteDir = remoteDir

    def upload(self, localPath):
        try:
            ftp = FTP(self.hostname, self.username, self.password)
            ftp.set_debuglevel(1)
            welcomeMsg = ftp.getwelcome()
            print(welcomeMsg)

            ftp.cwd(self.remoteDir)
            ftp.dir()

            # put file
            localFile = open(localPath, 'rb')
            try:
                ftp.storlines("STOR " + localFile.name, localFile)
                print("Put file %s is succeeded" % localFile)
            except error_temp:
                print("Put file is failed, time:%s<<" % time.strftime("%H:%M:%S"))
            finally:
                localFile.close()

        except Exception as ex:
            print("Can't connection given ftp server!", ex)
        finally:
            if ftp:
                ftp.close()


if __name__ == '__main__':
    imageUpload = ImageUpload('192.168.1.200', 'faceos', 'faceos', '/home/caveup0/')
    imageUpload.upload(r'C:\Users\xw80329\Desktop\data\test.jpg')
