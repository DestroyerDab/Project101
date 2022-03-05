import dropbox
class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken
    def upload_file(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.accessToken)
        f = open(fileFrom, "rb")
        dbx.files_upload(f.read(), fileTo)
def main():
    accessToken = "6YJVnsF_RBsAAAAAAAAAAV_qKn4F2n2IeaUd-gYFrYJTH1A-y08K3-36HE1pUGxf"
    transferData = TransferData(accessToken)
    fileFrom = input("Enter the name of the file to transfer")
    fileTo = input("Enter the path to be uploaded to")
    transferData.upload_file(fileFrom, fileTo)
    print("File has been moved")
main()