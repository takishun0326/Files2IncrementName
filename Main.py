import os

def renameFiles(input_path, ZERO_PADDING):

    files = os.listdir(input_path)

    # 1からインクリメント
    for i, file in enumerate(files, 1):

        # ファイル名と拡張子に分割
        root, ext = os.path.splitext(file)

        file_name = str(i).zfill(ZERO_PADDING) + ext
        print(file_name)
        os.rename(os.path.join(input_path, file), os.path.join(input_path, file_name))

def getInputPath():

    print("入力画像フォルダのパス")
    i_path = input(">> ")

    return i_path


if __name__ == "__main__":

    # ファイル名のゼロ埋め桁数
    ZERO_PADDING = 5

    input_path = getInputPath()
    renameFiles(input_path, ZERO_PADDING)