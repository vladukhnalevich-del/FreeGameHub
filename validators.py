from .constants import WEAK_PASSWORDS, SPECIAL_CHARS


def validate_password_strength(password):
    """Проверка сложности пароля"""
    errors = []

    # Проверка длины
    if len(password) < 8:
        errors.append("Пароль должен содержать минимум 8 символов")

    # Проверка наличия заглавной буквы
    if not any(c.isupper() for c in password):
        errors.append("Пароль должен содержать хотя бы одну заглавную букву")

    # Проверка наличия строчной буквы
    if not any(c.islower() for c in password):
        errors.append("Пароль должен содержать хотя бы одну строчную букву")

    # Проверка наличия цифры
    if not any(c.isdigit() for c in password):
        errors.append("Пароль должен содержать хотя бы одну цифру")

    # Проверка наличия специального символа
    if not any(c in SPECIAL_CHARS for c in password):
        errors.append("Пароль должен содержать хотя бы один специальный символ")

    # Проверка на простые пароли
    if password.lower() in WEAK_PASSWORDS:
        errors.append("Пароль слишком простой. Используйте более сложную комбинацию")

    # Проверка на последовательности
    if is_sequential(password):
        errors.append("Пароль содержит простые последовательности (abc, 123 и т.д.)")

    # Проверка на повторяющиеся символы
    if has_repeating_chars(password):
        errors.append("Пароль содержит слишком много повторяющихся символов")

    return errors


def is_sequential(password):
    """Проверка на последовательные символы"""
    password_lower = password.lower()

    # Проверка числовых последовательностей
    for i in range(len(password) - 2):
        if (password_lower[i].isdigit() and
                password_lower[i + 1].isdigit() and
                password_lower[i + 2].isdigit()):

            # Возрастающая последовательность
            if (ord(password_lower[i + 1]) - ord(password_lower[i]) == 1 and
                    ord(password_lower[i + 2]) - ord(password_lower[i + 1]) == 1):
                return True

            # Убывающая последовательность
            if (ord(password_lower[i]) - ord(password_lower[i + 1]) == 1 and
                    ord(password_lower[i + 1]) - ord(password_lower[i + 2]) == 1):
                return True

    # Проверка буквенных последовательностей
    for i in range(len(password) - 2):
        if (password_lower[i].isalpha() and
                password_lower[i + 1].isalpha() and
                password_lower[i + 2].isalpha()):

            if (ord(password_lower[i + 1]) - ord(password_lower[i]) == 1 and
                    ord(password_lower[i + 2]) - ord(password_lower[i + 1]) == 1):
                return True

    return False


def has_repeating_chars(password):
    """Проверка на повторяющиеся символы"""
    if len(password) < 4:
        return False

    # Проверка повторения одного символа
    for char in set(password):
        if password.count(char) > len(password) // 2:
            return True

    # Проверка паттернов типа "aaaa"
    for i in range(len(password) - 3):
        if password[i] == password[i + 1] == password[i + 2] == password[i + 3]:
            return True

    return False