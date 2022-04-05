Attribute VB_Name = "Module1"
' From https://www.extendoffice.com/documents/excel/3244-excel-remove-letters-from-strings-cells-numbers.html#:~:text=user%20defined%20function.-,Select%20a%20blank%20cell%20you%20will%20return%20the%20text%20string,the%20range%20as%20you%20need.

Function StripChar(Txt As String) As String
With CreateObject("VBScript.RegExp")
.Global = True
.Pattern = "\D"
StripChar = .Replace(Txt, "")
End With
End Function
