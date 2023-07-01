def guest_validate(text, author_name, author_email, status):
    errors = {}
    if not author_email:
        errors["author_email"] = "Поле обязательное"

    if not text:
        errors["text"] = "Поле обязательное"

    if not author_name:
        errors["author_name"] = "Поле обязательное"

    if not status:
        errors["status"] = "Поле обязательное"

    return errors