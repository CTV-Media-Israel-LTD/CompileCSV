#ifndef WINVER
#define WINVER 0x0600
#endif

#ifndef _WIN32_IE
#define _WIN32_IE 0x0700
#endif

#define UNICODE
#define _UNICODE
#include <windows.h>
#include <commctrl.h>
#include <string>
#include <vector>
#include <uxtheme.h>

#pragma comment(lib, "comctl32.lib")
#pragma comment(lib, "Comdlg32.lib")
#pragma comment(lib, "uxtheme.lib")

// Control IDs
#define ID_FILE_BUTTON_PD 1001
#define ID_FILE_BUTTON_STATIONS 1002
#define ID_FILE_BUTTON_PRIORITY 1003
#define ID_FILE_BUTTON_HOSTS 1012
#define ID_EDIT1 1004
#define ID_EDIT2 1005
#define ID_EDIT3 1006
#define ID_EDIT4 1013
#define ID_PD_PATH 1007
#define ID_STATIONS_PATH 1008
#define ID_PRIORITY_PATH 1009
#define ID_PROCESS_BUTTON 1010
#define ID_HOSTS_PATH 1011

// Global variables
HWND hEdit1, hEdit2, hEdit3, hEdit4;
HFONT hFont;
HBRUSH hButtonBrush, hEditBrush;

// Window procedure declaration
LRESULT CALLBACK WindowProcedure(HWND, UINT, WPARAM, LPARAM);

// Function to process files
void ProcessFiles();

// Function to create a styled button
HWND CreateStyledButton(HWND hParent, LPCWSTR text, int x, int y, int width, int height, HMENU hMenu);

// Function to create a styled static text
HWND CreateStyledStatic(HWND hParent, LPCWSTR text, int x, int y, int width, int height, HMENU hMenu);

// Function to create a styled edit control
HWND CreateStyledEdit(HWND hParent, int x, int y, int width, int height, HMENU hMenu);

// Custom window procedure for buttons
LRESULT CALLBACK ButtonProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam, UINT_PTR uIdSubclass, DWORD_PTR dwRefData);

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {
    // Initialize common controls
    INITCOMMONCONTROLSEX icex;
    icex.dwSize = sizeof(INITCOMMONCONTROLSEX);
    icex.dwICC = ICC_WIN95_CLASSES;
    InitCommonControlsEx(&icex);

    // Create custom font
    hFont = CreateFont(16, 0, 0, 0, FW_NORMAL, FALSE, FALSE, FALSE, ANSI_CHARSET,
        OUT_TT_PRECIS, CLIP_DEFAULT_PRECIS, DEFAULT_QUALITY,
        DEFAULT_PITCH | FF_DONTCARE, L"Segoe UI");

    // Create custom brushes
    hButtonBrush = CreateSolidBrush(RGB(0, 120, 215)); // Blue color
    hEditBrush = CreateSolidBrush(RGB(240, 240, 240)); // Light gray color

    // Register the window class
    const wchar_t CLASS_NAME[] = L"CSV Compiler Window Class";

    WNDCLASSEX wc = {};
    wc.cbSize = sizeof(WNDCLASSEX);
    wc.lpfnWndProc = WindowProcedure;
    wc.hInstance = hInstance;
    wc.lpszClassName = CLASS_NAME;
    wc.hbrBackground = (HBRUSH)(COLOR_WINDOW + 1);
    wc.hCursor = LoadCursor(NULL, IDC_ARROW);
    wc.hIcon = LoadIcon(NULL, IDI_APPLICATION);
    wc.hIconSm = LoadIcon(NULL, IDI_APPLICATION);

    RegisterClassEx(&wc);

    // Create the window
    HWND hwnd = CreateWindowEx(
        0,                          // Optional window styles
        CLASS_NAME,                 // Window class
        L"CSV Compiler",            // Window text
        WS_OVERLAPPEDWINDOW,        // Window style

        // Size and position
        CW_USEDEFAULT, CW_USEDEFAULT, 700, 600,

        NULL,       // Parent window
        NULL,       // Menu
        hInstance,  // Instance handle
        NULL        // Additional application data
    );

    if (hwnd == NULL) {
        return 0;
    }

    ShowWindow(hwnd, nCmdShow);
    UpdateWindow(hwnd);

    // Run the message loop
    MSG msg = {};
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    // Clean up
    DeleteObject(hFont);
    DeleteObject(hButtonBrush);
    DeleteObject(hEditBrush);

    return 0;
}

LRESULT CALLBACK WindowProcedure(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam) {
    switch (msg) {
    case WM_CREATE:
    {
        // Create the buttons and controls
        CreateStyledButton(hwnd, L"Select PlayerData CSV File", 20, 20, 250, 40, (HMENU)ID_FILE_BUTTON_PD);
        CreateStyledButton(hwnd, L"Select Stations CSV File", 20, 80, 250, 40, (HMENU)ID_FILE_BUTTON_STATIONS);
        CreateStyledButton(hwnd, L"Select Priority DB File", 20, 140, 250, 40, (HMENU)ID_FILE_BUTTON_PRIORITY);
        CreateStyledButton(hwnd, L"Select Hosts CSV File", 20, 200, 250, 40, (HMENU)ID_FILE_BUTTON_HOSTS);

        CreateStyledStatic(hwnd, L"PlayerData Path:", 20, 260, 120, 30, (HMENU)ID_PD_PATH);
        hEdit1 = CreateStyledEdit(hwnd, 150, 260, 520, 30, (HMENU)ID_EDIT1);

        CreateStyledStatic(hwnd, L"Stations Path:", 20, 310, 120, 30, (HMENU)ID_STATIONS_PATH);
        hEdit2 = CreateStyledEdit(hwnd, 150, 310, 520, 30, (HMENU)ID_EDIT2);

        CreateStyledStatic(hwnd, L"Priority Path:", 20, 360, 120, 30, (HMENU)ID_PRIORITY_PATH);
        hEdit3 = CreateStyledEdit(hwnd, 150, 360, 520, 30, (HMENU)ID_EDIT3);

        CreateStyledStatic(hwnd, L"Hosts Path:", 20, 410, 120, 30, (HMENU)ID_HOSTS_PATH);
        hEdit4 = CreateStyledEdit(hwnd, 150, 410, 520, 30, (HMENU)ID_EDIT4);

        // Create "Process Files" button
        CreateStyledButton(hwnd, L"Process Files", 20, 460, 250, 40, (HMENU)ID_PROCESS_BUTTON);

        break;
    }
    case WM_CTLCOLORSTATIC:
    {
        HDC hdcStatic = (HDC)wParam;
        SetTextColor(hdcStatic, RGB(0, 0, 0));
        SetBkMode(hdcStatic, TRANSPARENT);
        return (LRESULT)GetStockObject(NULL_BRUSH);
    }
    case WM_CTLCOLOREDIT:
    {
        HDC hdcEdit = (HDC)wParam;
        SetTextColor(hdcEdit, RGB(0, 0, 0));
        SetBkColor(hdcEdit, RGB(240, 240, 240));
        return (LRESULT)hEditBrush;
    }
case WM_COMMAND:
    {
        int wmId = LOWORD(wParam);
        switch (wmId) {
        case ID_FILE_BUTTON_PD:
        case ID_FILE_BUTTON_STATIONS:
        case ID_FILE_BUTTON_PRIORITY:
        case ID_FILE_BUTTON_HOSTS:
        {
            OPENFILENAME ofn;
            WCHAR szFile[260] = { 0 };
            ZeroMemory(&ofn, sizeof(ofn));
            ofn.lStructSize = sizeof(ofn);
            ofn.hwndOwner = hwnd;
            ofn.lpstrFile = szFile;
            ofn.nMaxFile = sizeof(szFile);
            ofn.lpstrFilter = L"CSV Files\0*.csv\0Excel Files\0*.xlsx;*.xls\0All Files\0*.*\0";
            ofn.nFilterIndex = 1;
            ofn.lpstrFileTitle = NULL;
            ofn.nMaxFileTitle = 0;
            ofn.lpstrInitialDir = NULL;
            ofn.Flags = OFN_PATHMUSTEXIST | OFN_FILEMUSTEXIST;

            if (GetOpenFileName(&ofn) == TRUE) {
                HWND hEditToSet = (wmId == ID_FILE_BUTTON_PD) ? hEdit1 :
                                  (wmId == ID_FILE_BUTTON_STATIONS) ? hEdit2 :
                                  (wmId == ID_FILE_BUTTON_PRIORITY) ? hEdit3 :
                                  hEdit4; // This is for ID_FILE_BUTTON_HOSTS
                SetWindowText(hEditToSet, ofn.lpstrFile);
            }
            break;
        }
        case ID_PROCESS_BUTTON:
        {
            ProcessFiles();
            break;
        }
        }
        break;
    }
    case WM_DESTROY:
        PostQuitMessage(0);
        break;
    default:
        return DefWindowProc(hwnd, msg, wParam, lParam);
    }
    return 0;
}

// Function to process files

void ProcessFiles() {
    std::wstring filePaths[4];
    wchar_t wbuffer[260];

    GetWindowText(hEdit1, wbuffer, 260);
    filePaths[0] = wbuffer;
    GetWindowText(hEdit2, wbuffer, 260);
    filePaths[1] = wbuffer;
    GetWindowText(hEdit3, wbuffer, 260);
    filePaths[2] = wbuffer;
    GetWindowText(hEdit4, wbuffer, 260);
    filePaths[3] = wbuffer;

    // Construct the command to run the Python script
    std::wstring command = L"python compile_csv.py";
    for (const auto& path : filePaths) {
        command += L" \"" + path + L"\"";
    }

    // Create a pipe for the child process's stdout
    HANDLE hReadPipe, hWritePipe;
    SECURITY_ATTRIBUTES saAttr = {sizeof(SECURITY_ATTRIBUTES)};
    saAttr.bInheritHandle = TRUE;
    saAttr.lpSecurityDescriptor = NULL;

    if (!CreatePipe(&hReadPipe, &hWritePipe, &saAttr, 0)) {
        MessageBox(NULL, L"Failed to create pipe", L"Error", MB_OK | MB_ICONERROR);
        return;
    }

    // Set up the start up info struct
    STARTUPINFO si = {sizeof(STARTUPINFO)};
    si.hStdOutput = hWritePipe;
    si.hStdError = hWritePipe;
    si.dwFlags |= STARTF_USESTDHANDLES;

    // Set up the process info struct
    PROCESS_INFORMATION pi = {0};

    // Create the child process
    if (!CreateProcess(NULL, &command[0], NULL, NULL, TRUE, 0, NULL, NULL, &si, &pi)) {
        MessageBox(NULL, L"Failed to create process", L"Error", MB_OK | MB_ICONERROR);
        CloseHandle(hReadPipe);
        CloseHandle(hWritePipe);
        return;
    }

    // Close the write end of the pipe
    CloseHandle(hWritePipe);

    // Read the output from the child process
    char buffer[4096];
    DWORD bytesRead;
    std::string output;

    while (ReadFile(hReadPipe, buffer, sizeof(buffer), &bytesRead, NULL) && bytesRead != 0) {
        output.append(buffer, bytesRead);
    }

    // Close handles
    CloseHandle(hReadPipe);
    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);

    // Convert output to wide string and display in a message box
    int size_needed = MultiByteToWideChar(CP_UTF8, 0, output.c_str(), -1, NULL, 0);
    std::wstring woutput(size_needed, 0);
    MultiByteToWideChar(CP_UTF8, 0, output.c_str(), -1, &woutput[0], size_needed);
    MessageBox(NULL, woutput.c_str(), L"Python Script Output", MB_OK | MB_ICONINFORMATION);
}

HWND CreateStyledButton(HWND hParent, LPCWSTR text, int x, int y, int width, int height, HMENU hMenu) {
    HWND hButton = CreateWindowEx(0, L"BUTTON", text, WS_VISIBLE | WS_CHILD | BS_OWNERDRAW, x, y, width, height, hParent, hMenu, NULL, NULL);
    SetWindowSubclass(hButton, ButtonProc, 0, 0);
    SendMessage(hButton, WM_SETFONT, (WPARAM)hFont, TRUE);
    return hButton;
}

HWND CreateStyledStatic(HWND hParent, LPCWSTR text, int x, int y, int width, int height, HMENU hMenu) {
    HWND hStatic = CreateWindowEx(0, L"STATIC", text, WS_VISIBLE | WS_CHILD, x, y, width, height, hParent, hMenu, NULL, NULL);
    SendMessage(hStatic, WM_SETFONT, (WPARAM)hFont, TRUE);
    return hStatic;
}

HWND CreateStyledEdit(HWND hParent, int x, int y, int width, int height, HMENU hMenu) {
    HWND hEdit = CreateWindowEx(0, L"EDIT", L"", WS_VISIBLE | WS_CHILD | WS_BORDER | ES_AUTOHSCROLL, x, y, width, height, hParent, hMenu, NULL, NULL);
    SendMessage(hEdit, WM_SETFONT, (WPARAM)hFont, TRUE);
    return hEdit;
}

LRESULT CALLBACK ButtonProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam, UINT_PTR uIdSubclass, DWORD_PTR dwRefData) {
    switch (msg) {
    case WM_PAINT:
    {
        PAINTSTRUCT ps;
        HDC hdc = BeginPaint(hwnd, &ps);

        RECT rc;
        GetClientRect(hwnd, &rc);

        // Fill background
        FillRect(hdc, &rc, hButtonBrush);

        // Draw text
        SetBkMode(hdc, TRANSPARENT);
        SetTextColor(hdc, RGB(255, 255, 255));

        WCHAR text[256];
        GetWindowText(hwnd, text, 256);

        DrawText(hdc, text, -1, &rc, DT_SINGLELINE | DT_CENTER | DT_VCENTER);

        // Draw rounded corners
        HPEN hPen = CreatePen(PS_SOLID, 1, RGB(0, 120, 215));
        SelectObject(hdc, hPen);
        SelectObject(hdc, GetStockObject(NULL_BRUSH));
        RoundRect(hdc, rc.left, rc.top, rc.right, rc.bottom, 10, 10);

        DeleteObject(hPen);
        EndPaint(hwnd, &ps);
        return 0;
    }
    }
    return DefSubclassProc(hwnd, msg, wParam, lParam);
}
