# portafolio/context_processors.py
def theme_from_cookie(request):
    theme = request.COOKIES.get("theme")   # 'light' | 'dark' | None
    if theme not in ("light", "dark"):
        theme = None
    return {"theme": theme}