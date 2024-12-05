Создать бота для сбора баллов ЕГЭ учеников через Telegram.
Описание задания:
Бот должен иметь следующие функции:


Регистрация ученика: Бот должен принимать запросы на регистрацию учеников и сохранять информацию о них в базе данных. Запрос на регистрацию должен содержать имя и фамилию ученика.
Ввод баллов ЕГЭ: Бот должен позволять ученикам вводить свои баллы ЕГЭ по различным предметам. Бот должен сохранять эти баллы в базе данных, связывая их с соответствующим учеником.
Просмотр баллов: Бот должен позволять ученикам просматривать свои сохраненные баллы ЕГЭ.

Бот должен быть развернут на платформе Telegram и иметь следующую функциональность:


Команда /start: При вводе этой команды бот должен приветствовать пользователя и предлагать ему зарегистрироваться или войти в свой аккаунт.
Команда /register: При вводе этой команды бот должен запрашивать у пользователя его имя, фамилию, а затем сохранять эту информацию в базе данных.
Команда /enter_scores: При вводе этой команды бот должен позволять ученику вводить свои баллы ЕГЭ. Бот должен запрашивать баллы и сохранять их в базе данных.
Команда /view_scores: При вводе этой команды бот должен выводить ученику его сохраненные баллы ЕГЭ.

База данных:


Используйте реляционную базу данных для хранения информации об учениках и их баллах ЕГЭ.
Стек:
Aiogram, SQLAlchemy, Alembic, Docker


Как предоставить ТЗ?

Необходимо продемонстрировать весь функционал бота (нажать на все кнопки). Это видео нужно добавить на гугл диск, открыть доступ “для всех”, чтобы мы смогли просмотреть видео и оценить его, а также необходимо прикрепить ссылку на код в гитхабе.