def get_username(request):
    try:
        username = request.user.username
    except:
        username = "незарегистрированный пользователь"
    return username