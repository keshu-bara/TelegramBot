import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes , CallbackContext


#importing tasks
from tasks import send_email
import logging

logging.basicConfig(level = logging.INFO,format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s')




#loading env varaibles for api key
load_dotenv()
API_KEY = os.getenv("API_KEY")



#invoke when the /start command is issued
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to the Appointment Bot! \n Use /help to see available commands.")


    

#invoke when the /help commad is issued
async def help(update: Update, context: CallbackContext):
    await update.message.reply_text("All help Commands:"
    "\n/start - Start the bot\n/help - Get help\n/book <emailid> - Book an appointment\n/cancel - Cancel an appointment\n/view - View your appointments\n/feedback - Send feedback\n/")


#booking appointment
async def book_appointment(update: Update, context: CallbackContext):
    user_date = update.message.from_user
    user_email = context.args[0] if context.args else None
    if not user_email:
        await update.message.reply_text("Please provide your email ID to book an appointment. Usage: /book <emailid>")
        return
    
    send_email(user_email)  # Call the task to send email
    logging.info(f"Booking appointment for {user_date.first_name} with email {user_email}")

    await update.message.reply_text(f"Booking an appointment... \n Name: {user_date.first_name} \n with email: {user_email} \n email will be send to your email address time and date of appointment.")

#canceling appointment
async def cancel_appointment(update: Update, context: CallbackContext):
    await update.message.reply_text("Cancelling your appointment...")

#viewing appointments
async def view_appointments(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are your appointments...")

#sending feedback
async def send_feedback(update: Update, context: CallbackContext):
    await update.message.reply_text("Sending your feedback...")






#adding handlers to the dispatcher



#Running the bot
if __name__ == "__main__":
    logging.info("Starting the bot...")
    #creating bot for the given token
    app = ApplicationBuilder().token(API_KEY).build()


    #adding handlers to the app
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("book", book_appointment))
    app.add_handler(CommandHandler("cancel", cancel_appointment))
    app.add_handler(CommandHandler("view", view_appointments))
    app.add_handler(CommandHandler("feedback", send_feedback))
    #app.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))
    app.run_polling()


def create_bot():
    logging.info("Starting the bot...")
    #creating bot for the given token
    app = ApplicationBuilder().token(API_KEY).build()


    #adding handlers to the app
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("book", book_appointment))
    app.add_handler(CommandHandler("cancel", cancel_appointment))
    app.add_handler(CommandHandler("view", view_appointments))
    app.add_handler(CommandHandler("feedback", send_feedback))
    #app.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))
    app.run_polling()
