# Warung Nusantara - Restaurant Ordering Application

## Overview

This is a Streamlit-based restaurant ordering application for "Warung Nusantara," an Indonesian restaurant. The application allows customers to browse the menu, add items to a shopping cart, place orders, and view order history. It's designed as a multi-page web application with a focus on Indonesian cuisine and Rupiah currency formatting.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Framework
- **Technology**: Streamlit (Python web framework)
- **Rationale**: Streamlit provides rapid prototyping for data-driven applications with minimal frontend code. It handles state management and UI rendering through Python.
- **Layout**: Wide layout with multi-page navigation using Streamlit's built-in pages system

### Application Structure
- **Pattern**: Multi-page Streamlit application with shared modules
- **Pages Location**: `pages/` directory with numbered files for navigation ordering
  - `1_Beranda.py` - Home/landing page with restaurant info
  - `2_Menu.py` - Menu browsing and item selection
  - `3_Pemesanan.py` - Shopping cart and checkout
  - `4_Riwayat.py` - Order history viewing

### State Management
- **Approach**: Streamlit's `st.session_state` for client-side state persistence
- **Key State Variables**:
  - `keranjang` (cart) - List storing current order items
  - `riwayat_pesanan` (order history) - List storing completed orders
- **Limitation**: State is session-based and not persisted to a database; data is lost on session end

### Data Layer
- **Current Implementation**: In-memory data storage using Python dictionaries and lists in `menu_data.py`
- **Menu Structure**: List of dictionaries with fields: id, nama (name), harga (price), deskripsi (description), kategori (category), tersedia (availability)
- **No Database**: Currently no persistent storage - all data is hardcoded

### Utility Functions
- **Module**: `utils.py` contains helper functions
- **Key Functions**:
  - `format_rupiah()` - Currency formatting for Indonesian Rupiah
  - `hitung_total_item()` - Calculate item total
  - `hitung_subtotal()` - Calculate order subtotal using loops

### Styling
- **Approach**: Custom CSS injected via `st.markdown()` with HTML styling
- **Design**: Gradient-based card designs with shadow effects, responsive layout

## External Dependencies

### Python Packages
- **Streamlit**: Core web framework for the entire application UI and routing
- **datetime**: Standard library for timestamp handling in orders

### No External Services
- No database connections
- No external APIs
- No authentication services
- No payment gateway integrations

### Future Considerations
If persistence is needed, consider adding:
- SQLite or PostgreSQL for order and menu storage
- User authentication for customer accounts
- Payment integration for real transactions