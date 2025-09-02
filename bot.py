import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

WELCOME_TEXT = (
	"Добро пожаловать в AdminPriority Bot 🎯\n"
	"Выберите раздел ниже 👇"
)

# URLs
URL_CREATE_DOCS = "https://chatgpt.com/g/g-68581034582c81919a0b0fc6d6c8719f-admin-documents"
URL_FIND_SUPPLIER = "https://adminpriority.ru"
URL_COURSES = "https://ai-adminpriority.ru"

# Callback data constants
CB_MAIN_MENU = "main_menu"
CB_SECTION_ADMIN = "section_admin"
CB_SECTION_PARTNER = "section_partner"

CB_ADMIN_CREATE_DOCS = "admin_create_docs"
CB_ADMIN_FIND_SUPPLIER = "admin_find_supplier"
CB_ADMIN_COURSES = "admin_courses"
CB_ADMIN_CONTACTS = "admin_contacts"

CB_PARTNER_FREE = "partner_free"
CB_PARTNER_PRICING = "partner_pricing"
CB_PARTNER_TZ = "partner_tz"
CB_PARTNER_AUDIENCE = "partner_audience"
CB_PARTNER_TIMELINE = "partner_timeline"
CB_PARTNER_CONTACTS = "partner_contacts"


def main_menu_keyboard() -> InlineKeyboardMarkup:
	keyboard = [
		[
			InlineKeyboardButton("Для админов, HR и закупщиков", callback_data=CB_SECTION_ADMIN)
		],
		[
			InlineKeyboardButton("Для партнёров", callback_data=CB_SECTION_PARTNER)
		],
	]
	return InlineKeyboardMarkup(keyboard)


def admin_menu_keyboard() -> InlineKeyboardMarkup:
	keyboard = [
		[InlineKeyboardButton("📄 Создать документы", callback_data=CB_ADMIN_CREATE_DOCS)],
		[InlineKeyboardButton("🔎 Найти поставщика", callback_data=CB_ADMIN_FIND_SUPPLIER)],
		[InlineKeyboardButton("🎓 Курсы и обучение", callback_data=CB_ADMIN_COURSES)],
		[InlineKeyboardButton("📞 Контакты", callback_data=CB_ADMIN_CONTACTS)],
		[InlineKeyboardButton("⬅️ Назад", callback_data=CB_MAIN_MENU)],
	]
	return InlineKeyboardMarkup(keyboard)


def partner_menu_keyboard() -> InlineKeyboardMarkup:
	keyboard = [
		[InlineKeyboardButton("🆓 Бесплатное размещение", callback_data=CB_PARTNER_FREE)],
		[InlineKeyboardButton("💼 Платные пакеты и реклама", callback_data=CB_PARTNER_PRICING)],
		[InlineKeyboardButton("📑 Технические задания (ТЗ)", callback_data=CB_PARTNER_TZ)],
		[InlineKeyboardButton("📊 Аудитория и статистика", callback_data=CB_PARTNER_AUDIENCE)],
		[InlineKeyboardButton("⏱ Сроки подключения", callback_data=CB_PARTNER_TIMELINE)],
		[InlineKeyboardButton("📞 Контакты для партнёров", callback_data=CB_PARTNER_CONTACTS)],
		[InlineKeyboardButton("⬅️ Назад", callback_data=CB_MAIN_MENU)],
	]
	return InlineKeyboardMarkup(keyboard)


async def send_welcome_with_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	if update.effective_chat:
		await context.bot.send_message(
			chat_id=update.effective_chat.id,
			text=WELCOME_TEXT,
			reply_markup=main_menu_keyboard(),
			disable_web_page_preview=True,
		)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	await send_welcome_with_menu(update, context)


async def handle_new_chat_members(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	await send_welcome_with_menu(update, context)


async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	# Any text triggers welcome + menu, per spec (no need to type /start)
	await send_welcome_with_menu(update, context)


async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	query = update.callback_query
	if not query:
		return
	await query.answer()

	data = query.data

	if data == CB_MAIN_MENU:
		await query.edit_message_text(WELCOME_TEXT, reply_markup=main_menu_keyboard(), disable_web_page_preview=True)
		return

	if data == CB_SECTION_ADMIN:
		text = "Раздел: Для админов, HR и закупщиков"
		await query.edit_message_text(text, reply_markup=admin_menu_keyboard(), disable_web_page_preview=True)
		return

	if data == CB_SECTION_PARTNER:
		text = "Раздел: Для партнёров"
		await query.edit_message_text(text, reply_markup=partner_menu_keyboard(), disable_web_page_preview=True)
		return

	# Admin submenu actions
	if data == CB_ADMIN_CREATE_DOCS:
		text = (
			"📄 Создать документы\n\n"
			f"Ссылка: {URL_CREATE_DOCS}\n\n"
			"Включите VPN.\n"
			"Проверяйте документы с юристами.\n"
			"⚠️ Не загружайте конфиденциальные данные."
		)
		await query.edit_message_text(text, reply_markup=admin_menu_keyboard(), disable_web_page_preview=True)
		return

	if data == CB_ADMIN_FIND_SUPPLIER:
		text = (
			"🔎 Найти поставщика\n\n"
			f"Ссылка: {URL_FIND_SUPPLIER}\n\n"
			"Каталог с 18 категориями (питание, офисы, безопасность, HR, подарки и др.).\n"
			"Все партнёры проходят проверку через ЭКГ-рейтинг.рф."
		)
		await query.edit_message_text(text, reply_markup=admin_menu_keyboard(), disable_web_page_preview=True)
		return

	if data == CB_ADMIN_COURSES:
		text = (
			"🎓 Курсы и обучение\n\n"
			f"Ссылка: {URL_COURSES}\n\n"
			"Обучаем команды работать с GPT и ИИ.\n"
			"• Подписчики журнала — 1 500 ₽\n"
			"• Не подписчики — 2 500 ₽\n"
			"• Корпоративное обучение (для админов, HR, юристов, маркетологов и др.) — цена по запросу."
		)
		await query.edit_message_text(text, reply_markup=admin_menu_keyboard(), disable_web_page_preview=True)
		return

	if data == CB_ADMIN_CONTACTS:
		text = (
			"📞 Контакты\n\n"
			"Вопросы: team@adminpriority.ru\n"
			"или чат поддержки на adminpriority.ru"
		)
		await query.edit_message_text(text, reply_markup=admin_menu_keyboard(), disable_web_page_preview=True)
		return

	# Partner submenu actions
	if data == CB_PARTNER_FREE:
		text = (
			"🆓 Бесплатное размещение\n\n"
			"Возможно бесплатное размещение.\n"
			"В платной версии:  \n"
			"- 1 рассылка в ежемесячном дайджесте  \n"
			"- Бегущая строка с логотипом  \n"
			"- Размещение логотипа на главной странице  \n"
			"- SEO продвижение  \n"
			"- Помощь в оформлении карточки  \n"
			"- Обучение 1 представителя компании GPT (3 часа)  \n"
			"- Размещение информации на первой странице"
		)
		await query.edit_message_text(text, reply_markup=partner_menu_keyboard(), disable_web_page_preview=True)
		return

	if data == CB_PARTNER_PRICING:
		text = (
			"💼 Платные пакеты и реклама\n\n"
			"• Размещение: 15 000 ₽ / 6 мес или 25 000 ₽ / год  \n"
			"• Логотип в бегущей строке или информация в дайджесте: 5 000 ₽ / мес  \n"
			"• Баннеры на главной странице: 25 000–40 000 ₽ / мес  \n"
			"(цены без НДС)"
		)
		await query.edit_message_text(text, reply_markup=partner_menu_keyboard(), disable_web_page_preview=True)
		return

	if data == CB_PARTNER_TZ:
		text = (
			"📑 Технические задания (ТЗ)\n\n"
			"• Каталог → https://clck.ru/3GYG4i  \n"
			"• Логотип (бегущая строка) → https://clck.ru/3GYG7A  \n"
			"• Изображение (дайджест) → https://clck.ru/3GYG9W  \n"
			"• Баннер «Максимальная выгода» → https://clck.ru/3GYFwn  \n"
			"• Баннер «Эффективное решение» → https://clck.ru/3GYG2j  \n"
			"• Баннер «Лучшее предложение» → https://clck.ru/3GYFrq  \n\n"
			"Все материалы отправляйте на team@adminpriority.ru"
		)
		await query.edit_message_text(text, reply_markup=partner_menu_keyboard(), disable_web_page_preview=True)
		return

	if data == CB_PARTNER_AUDIENCE:
		text = (
			"📊 Аудитория и статистика\n\n"
			"Ежемесячно сайт:  \n"
			"• Посетители: ~4 000  \n"
			"• Новые пользователи: 75–85%"
		)
		await query.edit_message_text(text, reply_markup=partner_menu_keyboard(), disable_web_page_preview=True)
		return

	if data == CB_PARTNER_TIMELINE:
		text = (
			"⏱ Сроки подключения\n\n"
			"Подключение за 2 рабочих дня.  \n"
			"Ответ придёт на почту или свяжется менеджер.  \n"
			"Срочные вопросы просьба писать: @marnlo с 11.00 до 19.00"
		)
		await query.edit_message_text(text, reply_markup=partner_menu_keyboard(), disable_web_page_preview=True)
		return

	if data == CB_PARTNER_CONTACTS:
		text = (
			"📞 Контакты для партнёров\n\n"
			"По вопросам размещения: team@adminpriority.ru"
		)
		await query.edit_message_text(text, reply_markup=partner_menu_keyboard(), disable_web_page_preview=True)
		return


def build_application() -> Application:
	if not BOT_TOKEN:
		raise RuntimeError("TELEGRAM_BOT_TOKEN is not set. Create .env with TELEGRAM_BOT_TOKEN=...")

	app = Application.builder().token(BOT_TOKEN).build()

	# Send greeting and menu without requiring /start
	app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, handle_new_chat_members))
	app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_message))

	# Optional /start handler
	app.add_handler(CommandHandler("start", start))

	# Callback queries for menus
	app.add_handler(CallbackQueryHandler(handle_callback))

	return app


def main() -> None:
	app = build_application()
	app.run_polling(allowed_updates=["message", "callback_query", "chat_member"])  # include membership updates


if __name__ == "__main__":
	main()

