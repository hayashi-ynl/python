Editor.FileSave();
Editor.ExecCommand("python " + '"' + Editor.GetFilename() + '"', 1)
// '"' はパスに空白が含まれている場合に有効