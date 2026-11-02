Использование:
python3 main.py <аргумент> <слово>

Режимы:
-lo    Легкая обфускация: инверсия регистра, случайный 4-значный хвост и спецсимвол.
-no    Нормальная обфускация: перемалывание основы слова через зеркальную матрицу замен и двойной случайный хвост.
-ho    Хардкорная обфускация: экстремальное запутывание через динамическую матрицу (Initialization-time) и случайный срез UUID4.
-h или --help     Вызов этой справки.

Результат:
Полиморфный высокоэнтропийный хаос. Из-за динамической сборки матриц замен через secrets каждый запуск утилиты выдает уникальный, непредсказуемый для брутфорсеров результат.

Usage:
python3 main.py <argv> <word>

Modes:
-lo    Lite obfuscation: inverts case, appends random 4-digit number and punctuation sign.
-no    Normal obfuscation: transforms word core via mirror-map with double random tail.
-ho    Hardcore obfuscation: extreme mutation via dynamic initialization map and random UUID4 slice.
-h or --help    Show this help message.

Output:
Polymorphic high-entropy chaos. Due to dynamic matrix initialization via secrets, every execution generates a unique, unpredictable result that completely breaks brute-force masks.
