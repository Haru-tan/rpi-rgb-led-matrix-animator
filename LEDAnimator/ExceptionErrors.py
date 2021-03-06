# ExceptionErrors.py
#
# User defined exceptions

# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass

class NotSupported(Error):
    """mode/type not supported"""
    pass

class MissingParameter(Error):
    """Raised when a required parameter is missing"""
    pass

class MissinImage(Error):
    """Raised when an image cannot be opened"""
    pass

class MissingImageTk(Error):
    """Raised when trying to import ImageTk"""
    pass

class NoImageData(Error):
    """Raised when importing an image in the ImageCache"""
    pass

class ImageLoadFailed(Error):
    """Raised when cv2.imread() returns None in the ImageCache"""
    pass

class PanelInitNotCalled(Error):
    """Panel must be initialised before calls are made to it """
    pass


class TextColorCombination(Error):
    """raised when both text foreground and background colours are None (pointless)"""
    pass

class AlphaChannelLost(Error):
    """raised when the software detects an alpha channel has been lost - coding error"""
    pass

class WindowOutOfBounds(Error):
    """ raised when a view of an image is out of bounds"""
    pass

class MethodNotImplemented(Error):
    """raised if an animation does not define the step() method"""
    pass

class InvalidColorTuple(Error):
    """colour tuples must be 3 or 4 digits rgb(a) """
    pass

class InvalidHexColor(Error):
    """Hex colour strings must be 6 hex digits (RRGGBB is assumed) """
    pass

class InvalidImageAlignmentMode(Error):
    """An incorrect alignement mode was specified"""
    pass

class InvalidMode(Error):
    """An incorrect mode was specified (Generic)"""
    pass

class Checkpoint(Error):
    """Used to halt execution when a checkpoint is reached"""
    pass

class AlphaBlendError(Error):
    """Used when two images to be blended are not the same shape"""
    pass

class NoSuchGlyph(Error):
    """Requested characetr does not exist in the character set of this font"""
    pass

class BDFFontSizeUnavailable(Error):
    """requested BDF font size is not available"""
    pass

class UnknownFontType(Error):
    """font type not recognised - see Constants.py for available types"""
    pass

class NoSuchMethod(Error):
    """ method requested is not supported in the helpwer/AntiAlias.py"""
    pass

class FileNotFound(Error):
    """attempt to access a disc file that doesn't exists"""
    pass

class InvalidScale(Error):
    """A scale value was given that is not in range"""
    pass

class UnsupportedFont(Error):
    """ A request was made for an unsupported font """
    pass