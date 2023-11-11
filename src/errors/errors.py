from werkzeug.exceptions import BadRequest, NotFound, Unauthorized, InternalServerError


def error_400(description: str) -> BadRequest:
    return BadRequest(description=description)


def error_404(description: str) -> NotFound:
    return NotFound(description=description)


def error_401(description: str) -> Unauthorized:
    return Unauthorized(description=description)


def error_500(description: str) -> InternalServerError:
    return InternalServerError(description=description)
