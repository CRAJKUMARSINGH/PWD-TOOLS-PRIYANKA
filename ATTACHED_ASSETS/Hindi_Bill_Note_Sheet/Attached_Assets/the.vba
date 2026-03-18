Option Explicit

' Add Windows API declarations for Unicode support
#If VBA7 Then
Private Declare PtrSafe Function SetWindowTextW Lib "user32" (ByVal hwnd As LongPtr, ByVal lpString As LongPtr) As Long
Private Declare PtrSafe Function GetWindowLongPtrW Lib "user32" (ByVal hwnd As LongPtr, ByVal nIndex As Long) As LongPtr
Private Declare PtrSafe Function SetWindowLongPtrW Lib "user32" (ByVal hwnd As LongPtr, ByVal nIndex As Long, ByVal dwNewLong As LongPtr) As LongPtr
#Else
Private Declare Function SetWindowTextW Lib "user32" (ByVal hwnd As Long, ByVal lpString As Long) As Long
Private Declare Function GetWindowLongA Lib "user32" (ByVal hwnd As Long, ByVal nIndex As Long) As Long
Private Declare Function SetWindowLongA Lib "user32" (ByVal hwnd As Long, ByVal nIndex As Long, ByVal dwNewLong As Long) As Long
#End If

Private Const GWL_STYLE As Long = -16
Private Const WS_HSCROLL As Long = &H100000
Private Const WS_VSCROLL As Long = &H200000
Const OUTPUT_CELL As String = "A40"

' Main function to generate Hindi Bill Notes
Sub GenerateHindiBillNotes_PerfectBulleted()
    Dim ws As Worksheet
    Set ws = ActiveSheet
    
    ' Set default font for Hindi text
    ws.Cells.Font.Name = "Mangal"
    
    '----------------------------
    ' Get data from cells
    '----------------------------
    Dim workOrderAmount As Double
    Dim uptoLastBill As Double
    Dim thisBill As Double
    Dim uptoDateBill As Double
    Dim percentageWorkDone As Double
    Dim startDate As Date
    Dim scheduleCompletion As Date
    Dim actualCompletion As Date
    Dim repairWork As String
    Dim extraItem As String
    Dim extraItemAmount As Double
    Dim excessQuantity As String
    Dim delayComment As String
    
    ' Initialize variables
    workOrderAmount = 0
    uptoLastBill = 0
    thisBill = 0
    uptoDateBill = 0
    percentageWorkDone = 0
    extraItemAmount = 0
    
    ' Get values from worksheet
    On Error Resume Next
    workOrderAmount = CDbl(ws.Range("C17").Value)
    uptoLastBill = CDbl(ws.Range("C18").Value)
    thisBill = CDbl(ws.Range("C19").Value)
    startDate = CDate(ws.Range("C12").Value)
    scheduleCompletion = CDate(ws.Range("C13").Value)
    actualCompletion = CDate(ws.Range("C14").Value)
    repairWork = Trim(ws.Range("C27").Value & "")
    extraItem = Trim(ws.Range("C25").Value & "")
    extraItemAmount = CDbl(ws.Range("C26").Value)
    excessQuantity = Trim(ws.Range("C28").Value & "")
    delayComment = Trim(ws.Range("C31").Value & "")
    On Error GoTo 0
    
    ' Calculate uptoDateBill
    If Val(ws.Range("C20").Value) > 0 Then
        uptoDateBill = Val(ws.Range("C20").Value)
    Else
        uptoDateBill = uptoLastBill + thisBill
    End If
    
    ' Calculate percentageWorkDone
    If workOrderAmount > 0 Then
        percentageWorkDone = (uptoDateBill / workOrderAmount) * 100
    End If
    
    '----------------------------
    ' Build Hindi Note with each item on new line (using vbLf for tight line spacing)
    '----------------------------
    Dim note As String
    Dim serialNumber As Integer
    serialNumber = 1
    note = ""
    
    ' Point 1: Work completion percentage
    note = BuildHindiLine(serialNumber, GetHindiText_WorkCompletion() & " " & Format(percentageWorkDone, "0.00") & " " & GetHindiText_Percent() & " " & GetHindiText_Completed())
    serialNumber = serialNumber + 1
    
    ' Point 2: Deviation handling based on work done percentage
    If percentageWorkDone < 90 Then
        note = note & vbLf & BuildHindiLine(serialNumber, GetHindiText_DeviationLess90())
        serialNumber = serialNumber + 1
    ElseIf percentageWorkDone > 100 Then
        note = note & vbLf & BuildHindiLine(serialNumber, GetHindiText_DeviationOver100())
        serialNumber = serialNumber + 1
    End If
    
    ' Point 3: Delay calculation
    Dim delayDays As Integer
    delayDays = DateDiff("d", scheduleCompletion, actualCompletion)
    
    If delayDays > 0 Then
        note = note & vbLf & BuildHindiLine(serialNumber, GetHindiText_WorkDelay() & " " & CStr(delayDays) & " " & GetHindiText_Days() & " " & GetHindiText_DelayOccurred())
        serialNumber = serialNumber + 1
        
        ' Time extension authority
        Dim scheduleDuration As Integer
        scheduleDuration = DateDiff("d", startDate, scheduleCompletion)
        
        If delayDays > scheduleDuration / 2 Then
            note = note & vbLf & BuildHindiLine(serialNumber, GetHindiText_TimeExtensionSE())
        Else
            note = note & vbLf & BuildHindiLine(serialNumber, GetHindiText_TimeExtensionLocal())
        End If
        serialNumber = serialNumber + 1
    Else
        note = note & vbLf & BuildHindiLine(serialNumber, GetHindiText_WorkOnTime())
        serialNumber = serialNumber + 1
    End If
    
    ' Point 4: Extra items handling
    If UCase(extraItem) = "YES" Then
        Dim extraItemPercentage As Double
        extraItemPercentage = (extraItemAmount / workOrderAmount) * 100
        
        If extraItemPercentage > 5 Then
            note = note & vbLf & BuildHindiLine(serialNumber, GetHindiText_ExtraItemOver5(extraItemAmount, extraItemPercentage))
        Else
            note = note & vbLf & BuildHindiLine(serialNumber, GetHindiText_ExtraItemUnder5(extraItemAmount, extraItemPercentage))
        End If
        serialNumber = serialNumber + 1
    End If
    
    ' Point 5: Excess quantity handling
    If UCase(excessQuantity) = "YES" Then
        If percentageWorkDone < 100 Then
            note = note & vbLf & BuildHindiLine(serialNumber, GetHindiText_ExcessQuantityWithSaving())
        ElseIf percentageWorkDone >= 100 And percentageWorkDone < 105 Then
            note = note & vbLf & BuildHindiLine(serialNumber, GetHindiText_ExcessQuantityUnder5(percentageWorkDone - 100))
        Else
            note = note & vbLf & BuildHindiLine(serialNumber, GetHindiText_ExcessQuantityOver5(percentageWorkDone - 100))
        End If
        serialNumber = serialNumber + 1
    End If
    
    ' Point 6: Quality control reports
    note = note & vbLf & BuildHindiLine(serialNumber, GetHindiText_QualityControl())
    serialNumber = serialNumber + 1
    
    ' Point 7: Hand over statement (if repair work is No)
    If UCase(repairWork) = "NO" Then
        note = note & vbLf & BuildHindiLine(serialNumber, GetHindiText_HandOver())
        serialNumber = serialNumber + 1
    End If
    
    ' Point 8: Bill submission delay comment (only when YES)
    If UCase(Trim(delayComment)) = "YES" Then
        note = note & vbLf & BuildHindiLine(serialNumber, GetHindiText_BillDelayComment())
        serialNumber = serialNumber + 1
    End If
    
    ' Final point: Conclusion
    note = note & vbLf & BuildHindiLine(serialNumber, GetHindiText_Conclusion())
    
    ' Add signature in Hindi - ???????? ???, AAO (inside note, will format separately)
    Dim signatureText As String
    signatureText = ChrW(2346) & ChrW(2381) & ChrW(2352) & ChrW(2375) & ChrW(2350) & ChrW(2354) & ChrW(2340) & ChrW(2366) & " " & ChrW(2332) & ChrW(2376) & ChrW(2344) & ", AAO"
    Dim noteLength As Integer
    noteLength = Len(note)  ' Length before adding signature
    ' 50mm right shift = approximately 35-40 spaces in Mangal font size 12
    note = note & vbLf & Space(40) & signatureText
    
    '----------------------------
    ' Output to worksheet
    '----------------------------
    On Error GoTo OutputError
    Application.ScreenUpdating = False
    
    ' First unmerge any existing merged cells in the area, then work with A40:D60
    On Error Resume Next
    ws.Range("A40:D60").UnMerge  ' Unmerge first in case it's merged
    On Error GoTo OutputError
    
    ' Clear the output area
    ws.Range("A40:D60").Clear
    
    ' Count number of lines in note to determine dynamic end row
    Dim lineCount As Integer
    Dim i As Long
    lineCount = 1  ' Start with 1 for first line
    For i = 1 To Len(note)
        If Mid(note, i, 1) = vbLf Then lineCount = lineCount + 1
    Next i
    
    ' Calculate end row (start at 40, add lines needed)
    Dim endRow As Integer
    endRow = 40 + lineCount + 2  ' Add buffer for wrapped text
    If endRow > 60 Then endRow = 60  ' Increased max limit
    
    ' Merge only required rows A40:D(endRow) for note with signature
    ws.Range("A40:D" & endRow).Merge
    
    ' Format and set value with wrap text
    With ws.Range("A40")
        .Value = note
        .NumberFormat = "@"
        .Font.Name = "Mangal"
        .Font.Size = 11
        .WrapText = True  ' Enable wrap text
        .VerticalAlignment = xlTop
        .HorizontalAlignment = xlLeft
    End With
    
    ' Format signature part - Bold and larger font
    Dim signatureStart As Integer
    signatureStart = noteLength + 2 + 40  ' +2 for vbLf, +40 for spaces (50mm shift)
    Dim signatureLen As Integer
    signatureLen = Len(signatureText)
    
    With ws.Range("A40").Characters(Start:=signatureStart, Length:=signatureLen).Font
        .Bold = True
        .Size = 12  ' One size larger
    End With
    
    ' Auto fit row height for merged area
    ws.Range("A40:D" & endRow).EntireRow.AutoFit
    
    ' Set dynamic print area from A1 to D(endRow)
    ws.PageSetup.PrintArea = "A1:D" & endRow
    
    ' Setup page for A4 printing - 10mm margins, dynamic bottom margin based on content
    ' Less content = more bottom margin (max 36mm), More content = less bottom margin (min 15mm)
    Dim bottomMarginMM As Double
    If lineCount <= 3 Then
        bottomMarginMM = 36  ' Maximum margin for minimal content
    ElseIf lineCount >= 9 Then
        bottomMarginMM = 15  ' Minimum margin for maximum content
    Else
        ' Linear interpolation between 36mm (3 lines) and 15mm (9 lines)
        bottomMarginMM = 36 - ((lineCount - 3) * (36 - 15) / (9 - 3))
    End If
    
    ' Ensure bottom margin stays within bounds (15mm to 36mm)
    If bottomMarginMM > 36 Then bottomMarginMM = 36
    If bottomMarginMM < 15 Then bottomMarginMM = 15
    
    With ws.PageSetup
        .PaperSize = xlPaperA4
        .Orientation = xlPortrait
        .FitToPagesWide = 1
        .FitToPagesTall = 1
        .LeftMargin = Application.CentimetersToPoints(1)                      ' 10mm = 1cm
        .RightMargin = Application.CentimetersToPoints(1)                     ' 10mm = 1cm
        .TopMargin = Application.CentimetersToPoints(1)                       ' 10mm = 1cm
        .BottomMargin = Application.CentimetersToPoints(bottomMarginMM / 10)  ' Dynamic bottom margin
        .Zoom = False  ' Use FitToPages instead of Zoom
    End With
    
    ' Generate filename: SheetName_Date_Time.pdf
    Dim pdfFileName As String
    Dim downloadsPath As String
    
    ' Get Downloads folder path
    downloadsPath = Environ("USERPROFILE") & "\Downloads\"
    
    ' Create filename with sheet name + date + time
    pdfFileName = downloadsPath & ws.Name & "_" & Format(Now, "DD-MM-YYYY_HH-MM") & ".pdf"
    
    ' Export to PDF
    ws.ExportAsFixedFormat Type:=xlTypePDF, _
                           Filename:=pdfFileName, _
                           Quality:=xlQualityStandard, _
                           IncludeDocProperties:=False, _
                           IgnorePrintAreas:=False, _
                           OpenAfterPublish:=True
    
    Application.ScreenUpdating = True
    MsgBox GetHindiText_Success() & vbCrLf & "PDF saved to: " & pdfFileName, vbInformation
    Exit Sub

OutputError:
    Application.ScreenUpdating = True
    MsgBox "Error generating Hindi note: " & Err.Description, vbCritical
End Sub
' Helper function to build numbered Hindi lines with simple space
Private Function BuildHindiLine(lineNum As Integer, text As String) As String
    BuildHindiLine = CStr(lineNum) & ". " & text
End Function

' Hindi text functions using Unicode characters
Private Function GetHindiText_WorkCompletion() As String
    ' ?????
    GetHindiText_WorkCompletion = ChrW(2325) & ChrW(2366) & ChrW(2352) & ChrW(2381) & ChrW(2351)
End Function

Private Function GetHindiText_Percent() As String
    ' ???????
    GetHindiText_Percent = ChrW(2346) & ChrW(2381) & ChrW(2352) & ChrW(2340) & ChrW(2367) & ChrW(2358) & ChrW(2340)
End Function

Private Function GetHindiText_Completed() As String
    ' ??????? ??? ???
    GetHindiText_Completed = ChrW(2360) & ChrW(2306) & ChrW(2346) & ChrW(2366) & ChrW(2342) & ChrW(2367) & ChrW(2340) & " " & _
                            ChrW(2361) & ChrW(2369) & ChrW(2310) & " " & ChrW(2361) & ChrW(2376) & ChrW(2404)
End Function

Private Function GetHindiText_DeviationLess90() As String
    ' ????? ??????? ????????? ?? ???????? ???? ??????? ??? ??, ????? ???????? ??? ???????? ?? ????????????? ??? ????? ???
    GetHindiText_DeviationLess90 = ChrW(2332) & ChrW(2367) & ChrW(2360) & ChrW(2325) & ChrW(2366) & " " & _
                                   ChrW(2337) & ChrW(2375) & ChrW(2357) & ChrW(2367) & ChrW(2319) & ChrW(2358) & ChrW(2344) & " " & _
                                   ChrW(2360) & ChrW(2381) & ChrW(2335) & ChrW(2375) & ChrW(2335) & ChrW(2350) & ChrW(2375) & ChrW(2306) & ChrW(2335) & " " & _
                                   ChrW(2349) & ChrW(2368) & " " & ChrW(2360) & ChrW(2381) & ChrW(2357) & ChrW(2368) & ChrW(2325) & ChrW(2371) & ChrW(2340) & ChrW(2367) & " " & _
                                   ChrW(2361) & ChrW(2375) & ChrW(2340) & ChrW(2369) & " " & ChrW(2346) & ChrW(2381) & ChrW(2352) & ChrW(2366) & ChrW(2346) & ChrW(2381) & ChrW(2340) & " " & _
                                   ChrW(2361) & ChrW(2369) & ChrW(2310) & " " & ChrW(2361) & ChrW(2376) & ", " & _
                                   ChrW(2332) & ChrW(2367) & ChrW(2360) & ChrW(2325) & ChrW(2368) & " " & _
                                   ChrW(2360) & ChrW(2381) & ChrW(2357) & ChrW(2368) & ChrW(2325) & ChrW(2371) & ChrW(2340) & ChrW(2367) & " " & _
                                   ChrW(2311) & ChrW(2360) & ChrW(2368) & " " & ChrW(2325) & ChrW(2366) & ChrW(2352) & ChrW(2381) & ChrW(2351) & ChrW(2366) & ChrW(2354) & ChrW(2351) & " " & _
                                   ChrW(2325) & ChrW(2375) & " " & ChrW(2325) & ChrW(2381) & ChrW(2359) & ChrW(2375) & ChrW(2340) & ChrW(2381) & ChrW(2352) & ChrW(2366) & ChrW(2343) & ChrW(2367) & ChrW(2325) & ChrW(2366) & ChrW(2352) & " " & _
                                   ChrW(2350) & ChrW(2375) & ChrW(2306) & " " & ChrW(2344) & ChrW(2367) & ChrW(2361) & ChrW(2367) & ChrW(2340) & " " & ChrW(2361) & ChrW(2376) & ChrW(2404)
End Function

Private Function GetHindiText_DeviationOver100() As String
    ' ????? ??????? ????????? ?? ???????? ???? ??????? ??? ??, OVERALL EXCESS ???? ????? ???? ?? 5% ?? ?? ?? ????? ???????? ??? ???????? ?? ????????????? ??? ????? ???
    GetHindiText_DeviationOver100 = ChrW(2332) & ChrW(2367) & ChrW(2360) & ChrW(2325) & ChrW(2366) & " " & _
                                    ChrW(2337) & ChrW(2375) & ChrW(2357) & ChrW(2367) & ChrW(2319) & ChrW(2358) & ChrW(2344) & " " & _
                                    ChrW(2360) & ChrW(2381) & ChrW(2335) & ChrW(2375) & ChrW(2335) & ChrW(2350) & ChrW(2375) & ChrW(2306) & ChrW(2335) & " " & _
                                    ChrW(2349) & ChrW(2368) & " " & ChrW(2360) & ChrW(2381) & ChrW(2357) & ChrW(2368) & ChrW(2325) & ChrW(2371) & ChrW(2340) & ChrW(2367) & " " & _
                                    ChrW(2361) & ChrW(2375) & ChrW(2340) & ChrW(2369) & " " & ChrW(2346) & ChrW(2381) & ChrW(2352) & ChrW(2366) & ChrW(2346) & ChrW(2381) & ChrW(2340) & " " & _
                                    ChrW(2361) & ChrW(2369) & ChrW(2310) & " " & ChrW(2361) & ChrW(2376) & ", " & _
                                    "OVERALL EXCESS " & ChrW(2357) & ChrW(2352) & ChrW(2381) & ChrW(2325) & " " & _
                                    ChrW(2310) & ChrW(2352) & ChrW(2381) & ChrW(2337) & ChrW(2352) & " " & ChrW(2352) & ChrW(2366) & ChrW(2358) & ChrW(2367) & " " & _
                                    ChrW(2325) & ChrW(2375) & " 5% " & ChrW(2360) & ChrW(2375) & " " & ChrW(2325) & ChrW(2350) & " " & _
                                    ChrW(2361) & ChrW(2376) & " " & ChrW(2332) & ChrW(2367) & ChrW(2360) & ChrW(2325) & ChrW(2368) & " " & _
                                    ChrW(2360) & ChrW(2381) & ChrW(2357) & ChrW(2368) & ChrW(2325) & ChrW(2371) & ChrW(2340) & ChrW(2367) & " " & _
                                    ChrW(2311) & ChrW(2360) & ChrW(2368) & " " & ChrW(2325) & ChrW(2366) & ChrW(2352) & ChrW(2381) & ChrW(2351) & ChrW(2366) & ChrW(2354) & ChrW(2351) & " " & _
                                    ChrW(2325) & ChrW(2375) & " " & ChrW(2325) & ChrW(2381) & ChrW(2359) & ChrW(2375) & ChrW(2340) & ChrW(2381) & ChrW(2352) & ChrW(2366) & ChrW(2343) & ChrW(2367) & ChrW(2325) & ChrW(2366) & ChrW(2352) & " " & _
                                    ChrW(2350) & ChrW(2375) & ChrW(2306) & " " & ChrW(2344) & ChrW(2367) & ChrW(2361) & ChrW(2367) & ChrW(2340) & " " & ChrW(2361) & ChrW(2376) & ChrW(2404)
End Function
Private Function GetHindiText_WorkDelay() As String
    ' ????? ???
    GetHindiText_WorkDelay = ChrW(2325) & ChrW(2366) & ChrW(2352) & ChrW(2381) & ChrW(2351) & " " & ChrW(2350) & ChrW(2375) & ChrW(2306)
End Function

Private Function GetHindiText_Days() As String
    ' ???
    GetHindiText_Days = ChrW(2342) & ChrW(2367) & ChrW(2344)
End Function

Private Function GetHindiText_DelayOccurred() As String
    ' ?? ???? ??? ???
    GetHindiText_DelayOccurred = ChrW(2325) & ChrW(2368) & " " & ChrW(2342) & ChrW(2375) & ChrW(2352) & ChrW(2368) & " " & _
                                ChrW(2361) & ChrW(2369) & ChrW(2312) & " " & ChrW(2361) & ChrW(2376) & ChrW(2404)
End Function

Private Function GetHindiText_TimeExtensionSE() As String
    ' ???? ????????? ??? Superintending Engineer, Electric Circle ???????? ?????? ???????? ???? ???? ???
    GetHindiText_TimeExtensionSE = ChrW(2335) & ChrW(2366) & ChrW(2311) & ChrW(2350) & " " & _
                                  ChrW(2319) & ChrW(2325) & ChrW(2381) & ChrW(2360) & ChrW(2335) & ChrW(2375) & ChrW(2306) & ChrW(2358) & ChrW(2344) & " " & _
                                  ChrW(2325) & ChrW(2375) & ChrW(2360) & " Superintending Engineer, PWD Electric Circle, Udaipur " & _
                                  ChrW(2325) & ChrW(2366) & ChrW(2352) & ChrW(2381) & ChrW(2351) & ChrW(2366) & ChrW(2354) & ChrW(2351) & " " & _
                                  ChrW(2342) & ChrW(2381) & ChrW(2357) & ChrW(2366) & ChrW(2352) & ChrW(2366) & " " & _
                                  ChrW(2309) & ChrW(2344) & ChrW(2369) & ChrW(2350) & ChrW(2379) & ChrW(2342) & ChrW(2367) & ChrW(2340) & " " & _
                                  ChrW(2325) & ChrW(2367) & ChrW(2351) & ChrW(2366) & " " & ChrW(2332) & ChrW(2366) & ChrW(2344) & ChrW(2366) & " " & ChrW(2361) & ChrW(2376) & ChrW(2404)
End Function

Private Function GetHindiText_TimeExtensionLocal() As String
    ' ???? ????????? ??? ?? ???????? ?????? ???????? ???? ???? ???
    GetHindiText_TimeExtensionLocal = ChrW(2335) & ChrW(2366) & ChrW(2311) & ChrW(2350) & " " & _
                                     ChrW(2319) & ChrW(2325) & ChrW(2381) & ChrW(2360) & ChrW(2335) & ChrW(2375) & ChrW(2306) & ChrW(2358) & ChrW(2344) & " " & _
                                     ChrW(2325) & ChrW(2375) & ChrW(2360) & " " & ChrW(2311) & ChrW(2360) & " " & _
                                     ChrW(2325) & ChrW(2366) & ChrW(2352) & ChrW(2381) & ChrW(2351) & ChrW(2366) & ChrW(2354) & ChrW(2351) & " " & _
                                     ChrW(2342) & ChrW(2381) & ChrW(2357) & ChrW(2366) & ChrW(2352) & ChrW(2366) & " " & _
                                     ChrW(2309) & ChrW(2344) & ChrW(2369) & ChrW(2350) & ChrW(2379) & ChrW(2342) & ChrW(2367) & ChrW(2340) & " " & _
                                     ChrW(2325) & ChrW(2367) & ChrW(2351) & ChrW(2366) & " " & ChrW(2332) & ChrW(2366) & ChrW(2344) & ChrW(2366) & " " & ChrW(2361) & ChrW(2376) & ChrW(2404)
End Function

Private Function GetHindiText_WorkOnTime() As String
    ' ????? ??? ?? ??????? ??? ???
    GetHindiText_WorkOnTime = ChrW(2325) & ChrW(2366) & ChrW(2352) & ChrW(2381) & ChrW(2351) & " " & _
                             ChrW(2360) & ChrW(2350) & ChrW(2351) & " " & ChrW(2346) & ChrW(2352) & " " & _
                             ChrW(2360) & ChrW(2306) & ChrW(2346) & ChrW(2366) & ChrW(2342) & ChrW(2367) & ChrW(2340) & " " & _
                             ChrW(2361) & ChrW(2369) & ChrW(2310) & " " & ChrW(2361) & ChrW(2376) & ChrW(2404)
End Function

Private Function GetHindiText_ExtraItemOver5(amount As Double, percentage As Double) As String
    ' ????? ??????? ??? ???? Rs. [amount] ???????? ???? ???????? ???? ??? ?? ????? ???? ???? ????? ???? ?? [percentage]% ???? 5% ?? ???? ?? ????? ???????? Superintending Engineer, Electric Circle ???????? ?? ????????????? ??? ???
    GetHindiText_ExtraItemOver5 = ChrW(2325) & ChrW(2366) & ChrW(2352) & ChrW(2381) & ChrW(2351) & " " & _
                                  ChrW(2360) & ChrW(2350) & ChrW(2381) & ChrW(2346) & ChrW(2366) & ChrW(2342) & ChrW(2344) & " " & _
                                  ChrW(2350) & ChrW(2375) & ChrW(2306) & " " & ChrW(2325) & ChrW(2375) & ChrW(2357) & ChrW(2354) & " Rs. " & _
                                  Format(amount, "0.00") & " " & _
                                  ChrW(2309) & ChrW(2340) & ChrW(2367) & ChrW(2352) & ChrW(2367) & ChrW(2325) & ChrW(2381) & ChrW(2340) & " " & _
                                  ChrW(2310) & ChrW(2311) & ChrW(2335) & ChrW(2350) & " " & _
                                  ChrW(2360) & ChrW(2350) & ChrW(2381) & ChrW(2346) & ChrW(2366) & ChrW(2342) & ChrW(2367) & ChrW(2340) & " " & _
                                  ChrW(2325) & ChrW(2367) & ChrW(2351) & ChrW(2366) & " " & ChrW(2327) & ChrW(2351) & ChrW(2366) & " " & _
                                  ChrW(2361) & ChrW(2376) & " " & ChrW(2332) & ChrW(2367) & ChrW(2360) & ChrW(2325) & ChrW(2368) & " " & _
                                  ChrW(2352) & ChrW(2366) & ChrW(2358) & ChrW(2367) & " " & ChrW(2357) & ChrW(2352) & ChrW(2381) & ChrW(2325) & " " & _
                                  ChrW(2310) & ChrW(2352) & ChrW(2381) & ChrW(2337) & ChrW(2352) & " " & ChrW(2352) & ChrW(2366) & ChrW(2358) & ChrW(2367) & " " & _
                                  ChrW(2325) & ChrW(2368) & " " & Format(percentage, "0.00") & "% " & _
                                  ChrW(2361) & ChrW(2379) & ChrW(2325) & ChrW(2352) & " 5% " & ChrW(2360) & ChrW(2375) & " " & _
                                  ChrW(2309) & ChrW(2343) & ChrW(2367) & ChrW(2325) & " " & ChrW(2361) & ChrW(2376) & " " & _
                                  ChrW(2332) & ChrW(2367) & ChrW(2360) & ChrW(2325) & ChrW(2368) & " " & _
                                  ChrW(2360) & ChrW(2381) & ChrW(2357) & ChrW(2368) & ChrW(2325) & ChrW(2371) & ChrW(2340) & ChrW(2367) & " " & _
                                  "Superintending Engineer, PWD Electric Circle, Udaipur " & _
                                  ChrW(2325) & ChrW(2366) & ChrW(2352) & ChrW(2381) & ChrW(2351) & ChrW(2366) & ChrW(2354) & ChrW(2351) & " " & _
                                  ChrW(2325) & ChrW(2375) & " " & ChrW(2325) & ChrW(2381) & ChrW(2359) & ChrW(2375) & ChrW(2340) & ChrW(2381) & ChrW(2352) & ChrW(2366) & ChrW(2343) & ChrW(2367) & ChrW(2325) & ChrW(2366) & ChrW(2352) & " " & _
                                  ChrW(2350) & ChrW(2375) & ChrW(2306) & " " & ChrW(2361) & ChrW(2376) & ChrW(2404)
End Function
Private Function GetHindiText_ExtraItemUnder5(amount As Double, percentage As Double) As String
    ' ????? ??????? ??? ???? Rs. [amount] ???????? ???? ???????? ???? ??? ?? ????? ???? ???? ????? ???? ?? [percentage]% ???? 5% ?? ?? ?? ????? ???????? ?? ???????? ?? ????????????? ??? ???
    GetHindiText_ExtraItemUnder5 = ChrW(2325) & ChrW(2366) & ChrW(2352) & ChrW(2381) & ChrW(2351) & " " & _
                                   ChrW(2360) & ChrW(2350) & ChrW(2381) & ChrW(2346) & ChrW(2366) & ChrW(2342) & ChrW(2344) & " " & _
                                   ChrW(2350) & ChrW(2375) & ChrW(2306) & " " & ChrW(2325) & ChrW(2375) & ChrW(2357) & ChrW(2354) & " Rs. " & _
                                   Format(amount, "0.00") & " " & _
                                   ChrW(2309) & ChrW(2340) & ChrW(2367) & ChrW(2352) & ChrW(2367) & ChrW(2325) & ChrW(2381) & ChrW(2340) & " " & _
                                   ChrW(2310) & ChrW(2311) & ChrW(2335) & ChrW(2350) & " " & _
                                   ChrW(2360) & ChrW(2350) & ChrW(2381) & ChrW(2346) & ChrW(2366) & ChrW(2342) & ChrW(2367) & ChrW(2340) & " " & _
                                   ChrW(2325) & ChrW(2367) & ChrW(2351) & ChrW(2366) & " " & ChrW(2327) & ChrW(2351) & ChrW(2366) & " " & _
                                   ChrW(2361) & ChrW(2376) & " " & ChrW(2332) & ChrW(2367) & ChrW(2360) & ChrW(2325) & ChrW(2368) & " " & _
                                   ChrW(2352) & ChrW(2366) & ChrW(2358) & ChrW(2367) & " " & ChrW(2357) & ChrW(2352) & ChrW(2381) & ChrW(2325) & " " & _
                                   ChrW(2310) & ChrW(2352) & ChrW(2381) & ChrW(2337) & ChrW(2352) & " " & ChrW(2352) & ChrW(2366) & ChrW(2358) & ChrW(2367) & " " & _
                                   ChrW(2325) & ChrW(2368) & " " & Format(percentage, "0.00") & "% " & _
                                   ChrW(2361) & ChrW(2379) & ChrW(2325) & ChrW(2352) & " 5% " & ChrW(2360) & ChrW(2375) & " " & _
                                   ChrW(2325) & ChrW(2350) & " " & ChrW(2361) & ChrW(2376) & " " & _
                                   ChrW(2332) & ChrW(2367) & ChrW(2360) & ChrW(2325) & ChrW(2368) & " " & _
                                   ChrW(2360) & ChrW(2381) & ChrW(2357) & ChrW(2368) & ChrW(2325) & ChrW(2371) & ChrW(2340) & ChrW(2367) & " " & _
                                   ChrW(2311) & ChrW(2360) & " " & ChrW(2325) & ChrW(2366) & ChrW(2352) & ChrW(2381) & ChrW(2351) & ChrW(2366) & ChrW(2354) & ChrW(2351) & " " & _
                                   ChrW(2325) & ChrW(2375) & " " & ChrW(2325) & ChrW(2381) & ChrW(2359) & ChrW(2375) & ChrW(2340) & ChrW(2381) & ChrW(2352) & ChrW(2366) & ChrW(2343) & ChrW(2367) & ChrW(2325) & ChrW(2366) & ChrW(2352) & " " & _
                                   ChrW(2350) & ChrW(2375) & ChrW(2306) & " " & ChrW(2361) & ChrW(2376) & ChrW(2404)
End Function

Private Function GetHindiText_ExcessQuantityWithSaving() As String
    ' ????? ?????? ??? ???? ????? ?? ??? ?????? ??? EXCESS QUANTITY ??????? ?? ?? ??, ???? ????? ?????? ??? ????? ??? saving ?? (?????? Overall Excess = NIL), ????? ???????? ?? ???????? ?? ????????????? ??? ???
    GetHindiText_ExcessQuantityWithSaving = ChrW(2325) & ChrW(2366) & ChrW(2352) & ChrW(2381) & ChrW(2351) & " " & _
                                           ChrW(2360) & ChrW(2306) & ChrW(2346) & ChrW(2366) & ChrW(2342) & ChrW(2344) & " " & _
                                           ChrW(2350) & ChrW(2375) & ChrW(2306) & " " & ChrW(2357) & ChrW(2352) & ChrW(2381) & ChrW(2325) & " " & _
                                           ChrW(2310) & ChrW(2352) & ChrW(2381) & ChrW(2337) & ChrW(2352) & " " & ChrW(2325) & ChrW(2375) & " " & _
                                           ChrW(2332) & ChrW(2367) & ChrW(2344) & " " & ChrW(2310) & ChrW(2311) & ChrW(2335) & ChrW(2350) & ChrW(2381) & ChrW(2360) & " " & _
                                           ChrW(2350) & ChrW(2375) & ChrW(2306) & " EXCESS QUANTITY " & _
                                           ChrW(2360) & ChrW(2306) & ChrW(2346) & ChrW(2366) & ChrW(2342) & ChrW(2367) & ChrW(2340) & " " & _
                                           ChrW(2325) & ChrW(2368) & " " & ChrW(2327) & ChrW(2312) & " " & ChrW(2361) & ChrW(2376) & ", " & _
                                           ChrW(2313) & ChrW(2344) & ChrW(2325) & ChrW(2366) & " " & ChrW(2357) & ChrW(2367) & ChrW(2357) & ChrW(2352) & ChrW(2339) & " " & _
                                           ChrW(2360) & ChrW(2306) & ChrW(2354) & ChrW(2327) & ChrW(2381) & ChrW(2344) & " " & ChrW(2361) & ChrW(2376) & ChrW(2404) & " " & _
                                           ChrW(2325) & ChrW(2366) & ChrW(2352) & ChrW(2381) & ChrW(2351) & " " & ChrW(2350) & ChrW(2375) & ChrW(2306) & " " & _
                                           "saving " & ChrW(2361) & ChrW(2376) & " " & _
                                           "(" & ChrW(2309) & ChrW(2352) & ChrW(2381) & ChrW(2341) & ChrW(2366) & ChrW(2340) & " OVERALL EXCESS NIL), " & _
                                           ChrW(2332) & ChrW(2367) & ChrW(2360) & ChrW(2325) & ChrW(2368) & " " & _
                                           ChrW(2360) & ChrW(2381) & ChrW(2357) & ChrW(2368) & ChrW(2325) & ChrW(2371) & ChrW(2340) & ChrW(2367) & " " & _
                                           ChrW(2311) & ChrW(2360) & " " & ChrW(2325) & ChrW(2366) & ChrW(2352) & ChrW(2381) & ChrW(2351) & ChrW(2366) & ChrW(2354) & ChrW(2351) & " " & _
                                           ChrW(2325) & ChrW(2375) & " " & ChrW(2325) & ChrW(2381) & ChrW(2359) & ChrW(2375) & ChrW(2340) & ChrW(2381) & ChrW(2352) & ChrW(2366) & ChrW(2343) & ChrW(2367) & ChrW(2325) & ChrW(2366) & ChrW(2352) & " " & _
                                           ChrW(2350) & ChrW(2375) & ChrW(2306) & " " & ChrW(2361) & ChrW(2376) & ChrW(2404)
End Function

Private Function GetHindiText_ExcessQuantityUnder5(excessPercent As Double) As String
    ' ????? ?????? ??? ???? ????? ?? ??? ?????? ??? EXCESS QUANTITY ??????? ?? ?? ??, ???? ????? ?????? ??? ????? ??? overall excess = ???? [excessPercent]% ???? 5% ?? ?? ??, ????? ???????? ?? ???????? ?? ????????????? ??? ???
    GetHindiText_ExcessQuantityUnder5 = ChrW(2325) & ChrW(2366) & ChrW(2352) & ChrW(2381) & ChrW(2351) & " " & _
                                        ChrW(2360) & ChrW(2306) & ChrW(2346) & ChrW(2366) & ChrW(2342) & ChrW(2344) & " " & _
                                        ChrW(2350) & ChrW(2375) & ChrW(2306) & " " & ChrW(2357) & ChrW(2352) & ChrW(2381) & ChrW(2325) & " " & _
                                        ChrW(2310) & ChrW(2352) & ChrW(2381) & ChrW(2337) & ChrW(2352) & " " & ChrW(2325) & ChrW(2375) & " " & _
                                        ChrW(2332) & ChrW(2367) & ChrW(2344) & " " & ChrW(2310) & ChrW(2311) & ChrW(2335) & ChrW(2350) & ChrW(2381) & ChrW(2360) & " " & _
                                        ChrW(2350) & ChrW(2375) & ChrW(2306) & " EXCESS QUANTITY " & _
                                        ChrW(2360) & ChrW(2306) & ChrW(2346) & ChrW(2366) & ChrW(2342) & ChrW(2367) & ChrW(2340) & " " & _
                                        ChrW(2325) & ChrW(2368) & " " & ChrW(2327) & ChrW(2312) & " " & ChrW(2361) & ChrW(2376) & ", " & _
                                        ChrW(2313) & ChrW(2344) & ChrW(2325) & ChrW(2366) & " " & ChrW(2357) & ChrW(2367) & ChrW(2357) & ChrW(2352) & ChrW(2339) & " " & _
                                        ChrW(2360) & ChrW(2306) & ChrW(2354) & ChrW(2327) & ChrW(2381) & ChrW(2344) & " " & ChrW(2361) & ChrW(2376) & ChrW(2404) & " " & _
                                        ChrW(2325) & ChrW(2366) & ChrW(2352) & ChrW(2381) & ChrW(2351) & " " & ChrW(2350) & ChrW(2375) & ChrW(2306) & " " & _
                                        "OVERALL EXCESS " & ChrW(2325) & ChrW(2375) & ChrW(2357) & ChrW(2354) & " " & _
                                        Format(excessPercent, "0.00") & "% " & _
                                        ChrW(2361) & ChrW(2379) & ChrW(2325) & ChrW(2352) & " 5% " & ChrW(2360) & ChrW(2375) & " " & _
                                        ChrW(2325) & ChrW(2350) & " " & ChrW(2361) & ChrW(2376) & ", " & _
                                        ChrW(2332) & ChrW(2367) & ChrW(2360) & ChrW(2325) & ChrW(2368) & " " & _
                                        ChrW(2360) & ChrW(2381) & ChrW(2357) & ChrW(2368) & ChrW(2325) & ChrW(2371) & ChrW(2340) & ChrW(2367) & " " & _
                                        ChrW(2311) & ChrW(2360) & " " & ChrW(2325) & ChrW(2366) & ChrW(2352) & ChrW(2381) & ChrW(2351) & ChrW(2366) & ChrW(2354) & ChrW(2351) & " " & _
                                        ChrW(2325) & ChrW(2375) & " " & ChrW(2325) & ChrW(2381) & ChrW(2359) & ChrW(2375) & ChrW(2340) & ChrW(2381) & ChrW(2352) & ChrW(2366) & ChrW(2343) & ChrW(2367) & ChrW(2325) & ChrW(2366) & ChrW(2352) & " " & _
                                        ChrW(2350) & ChrW(2375) & ChrW(2306) & " " & ChrW(2361) & ChrW(2376) & ChrW(2404)
End Function
Private Function GetHindiText_ExcessQuantityOver5(excessPercent As Double) As String
    ' ????? ?????? ??? ???? ????? ?? ??? ?????? ??? EXCESS QUANTITY ??????? ?? ?? ??, ???? ????? ?????? ??? ????? ??? overall excess = [excessPercent]% ???? 5% ?? ???? ??, ????? ???????? Superintending Engineer, Electric Circle ???????? ?? ????????????? ??? ???
    GetHindiText_ExcessQuantityOver5 = ChrW(2325) & ChrW(2366) & ChrW(2352) & ChrW(2381) & ChrW(2351) & " " & _
                                       ChrW(2360) & ChrW(2306) & ChrW(2346) & ChrW(2366) & ChrW(2342) & ChrW(2344) & " " & _
                                       ChrW(2350) & ChrW(2375) & ChrW(2306) & " " & ChrW(2357) & ChrW(2352) & ChrW(2381) & ChrW(2325) & " " & _
                                       ChrW(2310) & ChrW(2352) & ChrW(2381) & ChrW(2337) & ChrW(2352) & " " & ChrW(2325) & ChrW(2375) & " " & _
                                       ChrW(2332) & ChrW(2367) & ChrW(2344) & " " & ChrW(2310) & ChrW(2311) & ChrW(2335) & ChrW(2350) & ChrW(2381) & ChrW(2360) & " " & _
                                       ChrW(2350) & ChrW(2375) & ChrW(2306) & " EXCESS QUANTITY " & _
                                       ChrW(2360) & ChrW(2306) & ChrW(2346) & ChrW(2366) & ChrW(2342) & ChrW(2367) & ChrW(2340) & " " & _
                                       ChrW(2325) & ChrW(2368) & " " & ChrW(2327) & ChrW(2312) & " " & ChrW(2361) & ChrW(2376) & ", " & _
                                       ChrW(2313) & ChrW(2344) & ChrW(2325) & ChrW(2366) & " " & ChrW(2357) & ChrW(2367) & ChrW(2357) & ChrW(2352) & ChrW(2339) & " " & _
                                       ChrW(2360) & ChrW(2306) & ChrW(2354) & ChrW(2327) & ChrW(2381) & ChrW(2344) & " " & ChrW(2361) & ChrW(2376) & ChrW(2404) & " " & _
                                       ChrW(2325) & ChrW(2366) & ChrW(2352) & ChrW(2381) & ChrW(2351) & " " & ChrW(2350) & ChrW(2375) & ChrW(2306) & " " & _
                                       "OVERALL EXCESS " & Format(excessPercent, "0.00") & "% " & _
                                       ChrW(2361) & ChrW(2379) & ChrW(2325) & ChrW(2352) & " 5% " & ChrW(2360) & ChrW(2375) & " " & _
                                       ChrW(2309) & ChrW(2343) & ChrW(2367) & ChrW(2325) & " " & ChrW(2361) & ChrW(2376) & ", " & _
                                       ChrW(2332) & ChrW(2367) & ChrW(2360) & ChrW(2325) & ChrW(2368) & " " & _
                                       ChrW(2360) & ChrW(2381) & ChrW(2357) & ChrW(2368) & ChrW(2325) & ChrW(2371) & ChrW(2340) & ChrW(2367) & " " & _
                                       "Superintending Engineer, PWD Electric Circle, Udaipur " & _
                                       ChrW(2325) & ChrW(2366) & ChrW(2352) & ChrW(2381) & ChrW(2351) & ChrW(2366) & ChrW(2354) & ChrW(2351) & " " & _
                                       ChrW(2325) & ChrW(2375) & " " & ChrW(2325) & ChrW(2381) & ChrW(2359) & ChrW(2375) & ChrW(2340) & ChrW(2381) & ChrW(2352) & ChrW(2366) & ChrW(2343) & ChrW(2367) & ChrW(2325) & ChrW(2366) & ChrW(2352) & " " & _
                                       ChrW(2350) & ChrW(2375) & ChrW(2306) & " " & ChrW(2361) & ChrW(2376) & ChrW(2404)
End Function

Private Function GetHindiText_QualityControl() As String
    ' ???????? ???????? (Q.C.) ??????? ??????? ?????? ????
    GetHindiText_QualityControl = ChrW(2327) & ChrW(2369) & ChrW(2339) & ChrW(2357) & ChrW(2340) & ChrW(2381) & ChrW(2340) & ChrW(2366) & " " & _
                                 ChrW(2344) & ChrW(2367) & ChrW(2351) & ChrW(2306) & ChrW(2340) & ChrW(2381) & ChrW(2352) & ChrW(2339) & " " & _
                                 "(Q.C.) " & ChrW(2346) & ChrW(2352) & ChrW(2368) & ChrW(2325) & ChrW(2381) & ChrW(2359) & ChrW(2339) & " " & _
                                 ChrW(2352) & ChrW(2367) & ChrW(2346) & ChrW(2379) & ChrW(2352) & ChrW(2381) & ChrW(2335) & " " & _
                                 ChrW(2360) & ChrW(2306) & ChrW(2354) & ChrW(2327) & ChrW(2381) & ChrW(2344) & " " & ChrW(2361) & ChrW(2376) & ChrW(2306) & ChrW(2404)
End Function

Private Function GetHindiText_HandOver() As String
    ' ????????? ????? Hand Over Statement ?????? ???
    GetHindiText_HandOver = ChrW(2361) & ChrW(2360) & ChrW(2381) & ChrW(2340) & ChrW(2366) & ChrW(2306) & ChrW(2340) & ChrW(2352) & ChrW(2339) & " " & _
                           ChrW(2357) & ChrW(2367) & ChrW(2357) & ChrW(2352) & ChrW(2339) & " Hand Over Statement " & _
                           ChrW(2360) & ChrW(2306) & ChrW(2354) & ChrW(2327) & ChrW(2381) & ChrW(2344) & " " & ChrW(2361) & ChrW(2376) & ChrW(2404)
End Function

Private Function GetHindiText_BillDelayComment() As String
    ' ????? ??????? ?? ???? 6 ????? ??? ????? ??? ?? ???????? ??? ???????? ???? ??? ??? ?? ??????????? ???? ?? ??? ????? ??????? ?? ?????????? ????? ???, ??? ?????????? ???
    GetHindiText_BillDelayComment = ChrW(2325) & ChrW(2366) & ChrW(2352) & ChrW(2381) & ChrW(2351) & " " & _
                                    ChrW(2360) & ChrW(2350) & ChrW(2366) & ChrW(2346) & ChrW(2381) & ChrW(2340) & ChrW(2367) & " " & _
                                    ChrW(2325) & ChrW(2375) & " " & ChrW(2325) & ChrW(2352) & ChrW(2368) & ChrW(2348) & " 6 " & _
                                    ChrW(2350) & ChrW(2361) & ChrW(2368) & ChrW(2344) & ChrW(2375) & " " & ChrW(2348) & ChrW(2366) & ChrW(2342) & " " & _
                                    ChrW(2347) & ChrW(2366) & ChrW(2311) & ChrW(2344) & ChrW(2354) & " " & ChrW(2348) & ChrW(2367) & ChrW(2354) & " " & _
                                    ChrW(2311) & ChrW(2360) & " " & ChrW(2325) & ChrW(2366) & ChrW(2352) & ChrW(2381) & ChrW(2351) & ChrW(2366) & ChrW(2354) & ChrW(2351) & " " & _
                                    ChrW(2350) & ChrW(2375) & ChrW(2306) & " " & ChrW(2346) & ChrW(2381) & ChrW(2352) & ChrW(2360) & ChrW(2381) & ChrW(2340) & ChrW(2369) & ChrW(2340) & " " & _
                                    ChrW(2325) & ChrW(2367) & ChrW(2351) & ChrW(2366) & " " & ChrW(2327) & ChrW(2351) & ChrW(2366) & " " & ChrW(2361) & ChrW(2376) & ChrW(2404) & " " & _
                                    ChrW(2311) & ChrW(2360) & " " & ChrW(2309) & ChrW(2346) & ChrW(2381) & ChrW(2352) & ChrW(2340) & ChrW(2381) & ChrW(2351) & ChrW(2366) & ChrW(2358) & ChrW(2367) & ChrW(2340) & " " & _
                                    ChrW(2342) & ChrW(2375) & ChrW(2352) & ChrW(2368) & " " & ChrW(2325) & ChrW(2375) & " " & ChrW(2354) & ChrW(2367) & ChrW(2319) & " " & _
                                    ChrW(2360) & ChrW(2361) & ChrW(2366) & ChrW(2351) & ChrW(2325) & " " & ChrW(2309) & ChrW(2349) & ChrW(2367) & ChrW(2351) & ChrW(2306) & ChrW(2340) & ChrW(2366) & " " & _
                                    ChrW(2360) & ChrW(2375) & " " & ChrW(2360) & ChrW(2381) & ChrW(2346) & ChrW(2359) & ChrW(2381) & ChrW(2335) & ChrW(2368) & ChrW(2325) & ChrW(2352) & ChrW(2339) & " " & _
                                    ChrW(2350) & ChrW(2366) & ChrW(2306) & ChrW(2327) & ChrW(2366) & " " & ChrW(2332) & ChrW(2366) & ChrW(2319) & " " & _
                                    ChrW(2320) & ChrW(2360) & ChrW(2368) & " " & ChrW(2346) & ChrW(2381) & ChrW(2352) & ChrW(2360) & ChrW(2381) & ChrW(2340) & ChrW(2366) & ChrW(2357) & ChrW(2344) & ChrW(2366) & " " & ChrW(2361) & ChrW(2376) & ChrW(2404)
End Function

Private Function GetHindiText_NoBillDelay() As String
    ' ??? ???????????? ??? ??? ??????????? ???? ???? ???
    GetHindiText_NoBillDelay = ChrW(2348) & ChrW(2367) & ChrW(2354) & " " & _
                               ChrW(2346) & ChrW(2381) & ChrW(2352) & ChrW(2360) & ChrW(2381) & ChrW(2340) & ChrW(2369) & ChrW(2340) & ChrW(2368) & ChrW(2325) & ChrW(2352) & ChrW(2339) & " " & _
                               ChrW(2350) & ChrW(2375) & ChrW(2306) & " " & ChrW(2325) & ChrW(2379) & ChrW(2312) & " " & _
                               ChrW(2309) & ChrW(2346) & ChrW(2381) & ChrW(2352) & ChrW(2340) & ChrW(2381) & ChrW(2351) & ChrW(2366) & ChrW(2358) & ChrW(2367) & ChrW(2340) & " " & _
                               ChrW(2342) & ChrW(2375) & ChrW(2352) & ChrW(2368) & " " & ChrW(2344) & ChrW(2361) & ChrW(2368) & ChrW(2306) & " " & ChrW(2361) & ChrW(2376) & ChrW(2404)
End Function

Private Function GetHindiText_Conclusion() As String
    ' ??? ?????? ?????? ???? ???????? ???
    GetHindiText_Conclusion = ChrW(2348) & ChrW(2367) & ChrW(2354) & " " & _
                             ChrW(2360) & ChrW(2350) & ChrW(2369) & ChrW(2330) & ChrW(2367) & ChrW(2340) & " " & _
                             ChrW(2344) & ChrW(2367) & ChrW(2352) & ChrW(2381) & ChrW(2339) & ChrW(2351) & " " & _
                             ChrW(2361) & ChrW(2375) & ChrW(2340) & ChrW(2369) & " " & ChrW(2346) & ChrW(2381) & ChrW(2352) & ChrW(2360) & ChrW(2381) & ChrW(2340) & ChrW(2369) & ChrW(2340) & " " & ChrW(2361) & ChrW(2376) & ChrW(2404)
End Function

Private Function GetHindiText_Success() As String
    ' ????? ??? ??? ??????????? ????? ???? ???!
    GetHindiText_Success = ChrW(2361) & ChrW(2367) & ChrW(2306) & ChrW(2342) & ChrW(2368) & " " & _
                          ChrW(2348) & ChrW(2367) & ChrW(2354) & " " & ChrW(2344) & ChrW(2379) & ChrW(2335) & " " & _
                          ChrW(2360) & ChrW(2347) & ChrW(2354) & ChrW(2340) & ChrW(2366) & ChrW(2346) & ChrW(2370) & ChrW(2352) & ChrW(2381) & ChrW(2357) & ChrW(2325) & " " & _
                          ChrW(2340) & ChrW(2376) & ChrW(2351) & ChrW(2366) & ChrW(2352) & " " & ChrW(2325) & ChrW(2367) & ChrW(2351) & ChrW(2366) & " " & _
                          ChrW(2327) & ChrW(2351) & ChrW(2366) & "!"
End Function

' Helper function to clean text
Private Function CleanText(txt As String) As String
    txt = Replace(txt, vbCrLf, " ")
    txt = Replace(txt, vbCr, " ")
    txt = Replace(txt, vbLf, " ")
    Do While InStr(txt, "  ") > 0
        txt = Replace(txt, "  ", " ")
    Loop
    CleanText = Trim(txt)
End Function

