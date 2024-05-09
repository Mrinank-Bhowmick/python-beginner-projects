from app import App
from pathlib import Path

if __name__ == '__main__':
    db_path = Path(__file__).resolve().parent
    app = App(str(db_path / 'items.json'))
    app.mainloop()
    app.items_table.clear_test()
