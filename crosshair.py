import win32con
import win32gui
import win32api

def draw_crosshair(hdc, width, height):
    # Создаем красное перо толщиной 2 пикселя
    pen = win32gui.CreatePen(win32con.PS_SOLID, 2, win32api.RGB(255, 0, 0))
    size = 6  # Оптимальный размер прицела
    old_pen = win32gui.SelectObject(hdc, pen)
    
    center_x = width // 2
    center_y = height // 2
    
    # Горизонтальная линия
    win32gui.MoveToEx(hdc, center_x - size, center_y)
    win32gui.LineTo(hdc, center_x + size, center_y)

    # Вертикальная линия
    win32gui.MoveToEx(hdc, center_x, center_y - size)
    win32gui.LineTo(hdc, center_x, center_y + size)
    
    # Восстанавливаем старое перо
    win32gui.SelectObject(hdc, old_pen)
    win32gui.DeleteObject(pen)

def wndProc(hwnd, msg, wParam, lParam):
    if msg == win32con.WM_PAINT:
        hdc, paintStruct = win32gui.BeginPaint(hwnd)
        
        # Получаем размеры клиентской области
        rect = win32gui.GetClientRect(hwnd)
        width = rect[2] - rect[0]
        height = rect[3] - rect[1]
        
        # Рисуем прицел
        draw_crosshair(hdc, width, height)
        
        win32gui.EndPaint(hwnd, paintStruct)
        return 0
    elif msg == win32con.WM_DESTROY:
        win32gui.PostQuitMessage(0)
        return 0
    else:
        return win32gui.DefWindowProc(hwnd, msg, wParam, lParam)

def main():
    className = "CrosshairOverlay"
    hInstance = win32api.GetModuleHandle(None)
    
    # Регистрируем класс окна
    wndClass = win32gui.WNDCLASS()
    wndClass.hInstance = hInstance
    wndClass.lpszClassName = className
    wndClass.lpfnWndProc = wndProc
    wndClass.hCursor = win32gui.LoadCursor(None, win32con.IDC_ARROW)
    wndClass.hIcon = win32gui.LoadIcon(None, win32con.IDI_APPLICATION)
    wndClass.hbrBackground = win32gui.GetStockObject(win32con.BLACK_BRUSH)  # Черный фон
    
    win32gui.RegisterClass(wndClass)
    
    # Получаем размеры экрана
    screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

    # Создаем окно с нужными стилями
    hwnd = win32gui.CreateWindowEx(
        win32con.WS_EX_LAYERED | 
        win32con.WS_EX_TRANSPARENT | 
        win32con.WS_EX_TOPMOST |
        win32con.WS_EX_TOOLWINDOW,
        className,
        "Crosshair Overlay",
        win32con.WS_POPUP,
        0, 0, screen_width, screen_height,
        None, None, hInstance, None
    )
    
    # Устанавливаем прозрачность (черный цвет будет прозрачным)
    win32gui.SetLayeredWindowAttributes(hwnd, 0x000000, 0, win32con.LWA_COLORKEY)
    
    # Показываем окно
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
    win32gui.UpdateWindow(hwnd)
    
    # Главный цикл сообщений
    while True:
        msg = win32gui.GetMessage(None, 0, 0)
        if msg[0] == 0:  # WM_QUIT
            break
        win32gui.TranslateMessage(msg[1])
        win32gui.DispatchMessage(msg[1])

if __name__ == '__main__':
    main()
    