from http import HTTPStatus

HTTP_STATUS = {
    v: (v.phrase, v.description)
    for v in HTTPStatus.__members__.values()
}
