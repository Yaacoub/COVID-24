import platform
from subprocess import Popen, PIPE


class Global():
    """
    Class providing global utilities for the application,
    including managing full-screen mode.

    Methods:
    --------
    __darwin_or_x11() -> bool:
        Checks if the operating system is macOS or supports X11.
    set_full_screen(view, value=True):
        Configures the specified window to be in full-screen mode or normal mode.
    """

    def __darwin_or_x11(self):
        """
        Checks if the operating system is macOS or supports X11.

        Returns:
        --------
        bool:
            True if the system is macOS or supports X11, otherwise False.
        """
        if platform.system() == "Darwin":
            return True
        try:
            p = Popen(["xset", "-q"], stdout=PIPE, stderr=PIPE)
            p.communicate()
            return p.returncode == 0
        except Exception:
            return False

    def set_full_screen(self, view, value=True):
        """
        Configures the specified window to be in full-screen mode or normal mode.

        Parameters:
        ------------
        view : tk.Tk
            The window to configure.
        value : bool
            If True, configures the window in full-screen mode. Otherwise, in normal mode.
        """
        if self.__darwin_or_x11():
            view.attributes("-fullscreen", value)  # macOS
        else:
            view.state("zoomed" if value else "normal")  # Windows
        if platform.system() != "Linux":
            view.overrideredirect(True)
            view.resizable(width=False, height=False)