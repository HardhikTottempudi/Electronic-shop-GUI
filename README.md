# 🛒 Electronic Shop Management System

A comprehensive **Python-based GUI application** for managing an electronics retail shop with integrated MySQL database support, user authentication, and invoice generation capabilities.

## 🌟 Features

### Core Functionality
- **Interactive GUI**: Built with Tkinter for intuitive shop management
- **User Authentication System**: Secure login/signup with password protection
- **Member Discount System**: 15% discount for registered members
- **Product Management**: Add, view, and delete products from the bill
- **Real-time Bill Calculation**: Automatic price calculation with discount application
- **Database Integration**: MySQL backend for persistent data storage

### Key Capabilities
- Customer registration with username/password
- Shopping cart management
- Dynamic bill generation
- Product inventory tracking
- User session management

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **GUI Framework**: Tkinter
- **Database**: MySQL
- **Libraries**:
  - `mysql-connector-python` - Database connectivity
  - `tkinter.ttk` - Enhanced UI components
  - `smtplib` - Email functionality

## 📋 Prerequisites

- Python 3.x installed
- MySQL Server installed and running
- Required Python packages:
  ```bash
  pip install mysql-connector-python
  ```

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/HardhikTottempudi/Electronic-shop-GUI.git
   cd Electronic-shop-GUI
   ```

2. **Set up MySQL database**
   ```bash
   mysql -u root -p < electronic_app.sql
   ```

3. **Configure database credentials**
   
   Open `main.py` and update the database connection settings:
   ```python
   db = mysql.connector.connect(
     host="localhost",
     user="root",
     password="YOUR_PASSWORD",  # Update this
     database="12b_hardhik"
   )
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

## 💡 Usage

1. **Launch the application** - Run `main.py` to open the main shop interface
2. **Sign Up/Login** - Create an account or login to access member discounts
3. **Add Products** - Browse and add items to your bill
4. **Manage Cart** - View, edit, or delete items from the cart
5. **Checkout** - Generate final bill with automatic discount application

## 📊 Database Schema

The application uses the following tables:
- `login_data`: Stores user authentication information
- `bill`: Temporary storage for current shopping session
- `bill_final`: Finalized bills with serial numbers

## 🎯 Key Features for Hiring Managers

- **Full-Stack Development**: Demonstrates proficiency in frontend (GUI) and backend (database) integration
- **Security**: Implements password protection and user authentication
- **Database Design**: Shows understanding of relational database concepts
- **Real-World Application**: Practical retail management solution
- **Clean Code Structure**: Organized, maintainable codebase with modular functions

## 🔮 Future Enhancements

- Integration with payment gateways
- Enhanced reporting and analytics
- Product search and filter functionality
- Email invoice generation
- Multi-store support

## 📝 License

This project is open source and available for educational purposes.

## 👤 Author

**Hardhik Tottempudi**
- GitHub: [@HardhikTottempudi](https://github.com/HardhikTottempudi)
- Portfolio: [hardhiktottempudi.com](https://hardhiktottempudi.com/)

---

*This project demonstrates practical application of Python GUI development and database management skills.*
