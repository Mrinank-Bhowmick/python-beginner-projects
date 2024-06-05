from tkinter import messagebox
import customtkinter as ctk

from datetime import datetime
from pathlib import Path

from gui_widgets import ItemsTable, SummaryByCategoryPivotTable
from item import ItemsDB, Category, Item
from expense_income_stats import ExcelReport, PdfReport


class App(ctk.CTk):
    """
    Represents the main application for managing expenses.

    This class provides a GUI application for adding, updating, and deleting expense items,
    generating reports, and visualizing data.
    """

    def __init__(self, db_path, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configure Main Window
        self.title("Expense Tracker")
        self.geometry("1500x730")

        # Configure Layout
        self.grid_rowconfigure((0, 1, 2, 3), weight=2)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        # ==============================================================================================================

        # Table for the Expense Items
        self._items_db = ItemsDB(db_path)
        self.items_table = ItemsTable(self, self._items_db)
        self.items_table.grid(
            row=0, column=0, padx=5, pady=5, columnspan=3, sticky="nswe"
        )
        self.items_table.bind("<ButtonRelease-1>", self.on_row_selected)

        # ==============================================================================================================
        # Settings Tab
        # Unfortunately, Customtkinter does not support menu bar
        self.tab_view_settings = ctk.CTkTabview(self)
        self.tab_view_settings.grid(row=1, column=0, padx=5, pady=5, sticky="nswe")

        # Edit Tab
        self.tab_view_settings.add("Edit")

        button = ctk.CTkButton(
            self.tab_view_settings.tab("Edit"),
            text="Deselect Table",
            command=lambda: self.items_table.deselect(),
        )
        button.pack(pady=5)

        button = ctk.CTkButton(
            self.tab_view_settings.tab("Edit"),
            text="Update Summaries",
            command=self.update_pivot_tables,
        )
        button.pack(pady=5)

        # Report Tab
        self.tab_view_settings.add("Report")

        self.btn_generate_excel_report = ctk.CTkButton(
            self.tab_view_settings.tab("Report"),
            text="Generate Excel Report",
            command=self.generate_excel_report,
        )
        self.btn_generate_excel_report.pack(pady=5)

        self.btn_generate_pdf_report = ctk.CTkButton(
            self.tab_view_settings.tab("Report"),
            text="Generate PDF Report",
            command=self.generate_pdf_report,
        )
        self.btn_generate_pdf_report.pack(pady=5)

        # Set Default Tab to 'Edit'
        self.tab_view_settings.set("Edit")

        # ==============================================================================================================

        # Frame for Buttons
        self.frame_buttons = ctk.CTkFrame(self, border_color="black")
        self.frame_buttons.grid(row=1, column=1, padx=5, pady=5)

        # Add Button
        self.btn_add_item = ctk.CTkButton(
            self.frame_buttons,
            text="Add",
            command=self.on_btn_add_clicked,
        )
        self.btn_add_item.pack(padx=5, pady=5)

        # Update Button
        self.btn_update_item = ctk.CTkButton(
            self.frame_buttons,
            text="Update",
            command=self.on_btn_update_clicked,
        )
        self.btn_update_item.pack(padx=5, pady=5)

        # Delete Button
        self.btn_delete_item = ctk.CTkButton(
            self.frame_buttons,
            text="Delete",
            command=self.on_btn_delete_clicked,
        )
        self.btn_delete_item.pack(padx=5, pady=5)

        # Clear Form Button
        self.btn_clear_form = ctk.CTkButton(
            self.frame_buttons,
            text="Clear Form",
            command=self.clear_form,
        )
        self.btn_clear_form.pack(padx=5, pady=5)

        # ==============================================================================================================

        # Frame for Form
        self.frame_form = ctk.CTkFrame(self, border_color="black")
        self.frame_form.grid(row=1, column=2, padx=5, pady=5, ipadx=10, sticky="nswe")
        self.frame_form.grid_rowconfigure([i for i in range(6)], weight=1)
        self.frame_form.grid_columnconfigure((0, 1), weight=1)

        # Entry - Name
        label = ctk.CTkLabel(self.frame_form, text="Name: ", fg_color="transparent")
        label.grid(row=0, column=0, padx=5, pady=5, sticky="we")
        self.entry_name = ctk.CTkEntry(self.frame_form, placeholder_text="Name")
        self.entry_name.grid(row=0, column=1, padx=5, pady=5, sticky="we")

        # Entry - Amount
        label = ctk.CTkLabel(self.frame_form, text="Amount: ", fg_color="transparent")
        label.grid(row=1, column=0, padx=5, pady=5, sticky="we")
        self.entry_amount = ctk.CTkEntry(self.frame_form, placeholder_text="Amount")
        self.entry_amount.grid(row=1, column=1, padx=5, pady=5, sticky="we")

        # Entry - Description
        label = ctk.CTkLabel(
            self.frame_form, text="Description: ", fg_color="transparent"
        )
        label.grid(row=2, column=0, padx=5, pady=5, sticky="we")
        self.entry_description = ctk.CTkEntry(
            self.frame_form, placeholder_text="Description"
        )
        self.entry_description.grid(row=2, column=1, padx=5, pady=5, sticky="we")

        # Entry - Date
        label = ctk.CTkLabel(self.frame_form, text="Date: ", fg_color="transparent")
        label.grid(row=3, column=0, padx=5, pady=5, sticky="we")
        self.entry_date = ctk.CTkEntry(self.frame_form, placeholder_text="YYYY-MM-dd")
        self.entry_date.grid(row=3, column=1, padx=5, pady=5, sticky="we")

        # Entry - Category
        label = ctk.CTkLabel(self.frame_form, text="Category: ", fg_color="transparent")
        label.grid(row=4, column=0, padx=5, pady=5, sticky="we")
        self.entry_category = ctk.CTkEntry(self.frame_form, placeholder_text="Category")
        self.entry_category.grid(row=4, column=1, padx=5, pady=5, sticky="we")

        # Entry - Subcategory
        label = ctk.CTkLabel(
            self.frame_form, text="Subcategory: ", fg_color="transparent"
        )
        label.grid(row=5, column=0, padx=5, pady=5, sticky="we")
        self.entry_subcategory = ctk.CTkEntry(
            self.frame_form, placeholder_text="Subcategory"
        )
        self.entry_subcategory.grid(row=5, column=1, padx=5, pady=5, sticky="we")

        # ==============================================================================================================

        # CTkTabview for Visualizations
        self.tab_view_visuals = ctk.CTkTabview(self)
        self.tab_view_visuals.grid(
            row=2, column=0, padx=5, pady=5, columnspan=3, sticky="nswe"
        )

        expense_tab = self.tab_view_visuals.add(
            "Summary By Category"
        )  # Summary By Category Tab

        self.tab_view_visuals.set("Summary By Category")  # set currently visible tab

        # Summary By Category Tab Contents
        self.pivot_table = SummaryByCategoryPivotTable(
            self.tab_view_visuals.tab("Summary By Category")
        )

        # ==============================================================================================================
        # Other Widget-Event-Callbacks Bindings
        self.protocol("WM_DELETE_WINDOW", self.on_window_close)

    def update_pivot_tables(self):
        """Updates the pivot tables."""

        self.pivot_table.update_pivot_table()

    def generate_excel_report(self):
        """Generates an Excel report."""

        excel_path = str(Path(__file__).resolve().parent / "report.xlsx")
        report = ExcelReport(excel_path, self._items_db)
        report.generate_report()

    def generate_pdf_report(self):
        """Generates a PDF report."""

        pdf_path = str(Path(__file__).resolve().parent / "report.pdf")
        report = PdfReport(pdf_path, self._items_db)
        report.generate_report()

    def on_window_close(self):
        """Callback for window close event."""

        # Reference: https://stackoverflow.com/questions/111155/how-do-i-handle-the-window-close-event-in-tkinter
        print("Window Closing ...")
        self.destroy()

    def _get_form_values(self):
        """Returns a Dictionary of the Form Values"""
        return {
            "name": self.entry_name.get(),
            "amount": self.entry_amount.get(),
            "description": self.entry_description.get(),
            "date": self.entry_date.get(),
            "category": self.entry_category.get(),
            "subcategory": self.entry_subcategory.get(),
        }

    def clear_form(self):
        """Clears the form."""

        self.entry_name.delete(0, last_index=len(self.entry_name.get()))
        self.entry_amount.delete(0, last_index=len(self.entry_amount.get()))
        self.entry_description.delete(0, last_index=len(self.entry_description.get()))
        self.entry_date.delete(0, last_index=len(self.entry_date.get()))
        self.entry_category.delete(0, last_index=len(self.entry_category.get()))
        self.entry_subcategory.delete(0, last_index=len(self.entry_subcategory.get()))

    def fill_form(
        self, name, amount, description, date, category="None", subcategory="None"
    ):
        """Fills the form with provided values."""

        self.clear_form()
        self.entry_name.insert(0, name)
        self.entry_amount.insert(0, amount)
        self.entry_date.insert(0, date)
        self.entry_description.insert(0, description)
        self.entry_category.insert(0, category)
        self.entry_subcategory.insert(0, subcategory)

    def on_btn_add_clicked(self):
        """Callback for add button click event."""

        new_item = self._create_item_from_form()

        if new_item is not None:
            self.items_table.add_item(new_item)
        else:
            messagebox.showerror("Error", "Invalid Item Data")

        self.clear_form()

    def on_btn_update_clicked(self):
        """Callback for update button click event."""

        # Get the (one) selected item
        selected_item = self.items_table.focus()
        item_dct = self.items_table.item(selected_item)
        values = item_dct["values"]
        item_id = item_dct["text"]
        row = [item_id] + list(values)

        try:
            item_obj = self._create_item(row)
        except IndexError:
            self.items_table.deselect()
            messagebox.showerror("Error", "Invalid Action")
            return

        # Reconstruct the Forms
        try:
            item_obj.name = self.entry_name.get().strip()
            item_obj.amount = float(self.entry_amount.get().strip())
            item_obj.description = self.entry_description.get().strip()
            item_obj.date = datetime.strptime(
                self.entry_date.get().strip(), "%Y-%m-%d %H:%M:%S"
            )
            item_obj.category = (
                None
                if self.entry_category.get() == "None"
                else (
                    Category(self.entry_category.get().strip())
                    if self.entry_subcategory.get().strip() == "None"
                    else Category(
                        self.entry_category.get().strip(),
                        self.entry_subcategory.get().strip(),
                    )
                )
            )

        except ValueError as value_error:
            messagebox.showerror("Error", str(value_error))
            return

        # Update Local Data and View
        self.items_table.update_item(item_obj)

        self.clear_form()

    def on_btn_delete_clicked(self):
        """Callback for delete button click event."""

        yes_or_no = messagebox.askyesno("Delete Item", "Do you want to continue?")

        if not yes_or_no:
            self.items_table.deselect()
            return

        self.clear_form()

        if len(self.items_table.selection()) == 0:
            return

        items = (self.items_table.item(item) for item in self.items_table.selection())
        items = ([item["text"]] + list(item["values"]) for item in items)

        item_objs = [self._create_item(item) for item in items]

        self.items_table.deletes_item(item_objs)

    def _create_item(self, inp_item):
        """
        Creates an item from input.

        Args:
            inp_item (List[str|int|float]): List representing an item.
        """

        try:
            item_id = inp_item[0]
            item_name = inp_item[1]
            item_amount = inp_item[2]
            item_description = inp_item[3]
            item_date = inp_item[4]
            item_category = inp_item[5]
            item_subcategory = inp_item[6]

            # Clean Date
            item_date = datetime.strptime(item_date, "%Y-%m-%d %H:%M:%S")

            if item_category in ["None", ""]:
                category = None
            else:
                if item_subcategory in ["None", ""]:
                    category = Category(item_category)
                else:
                    category = Category(item_category, item_subcategory)

            item_obj = Item(
                item_id, item_name, item_amount, item_description, item_date, category
            )

            return item_obj
        except ValueError:
            return None

    def _create_item_from_form(self) -> Item | None:
        """Creates an item from the form."""

        try:
            if self.entry_category.get().strip() in ["None", ""]:
                category = None
            else:
                entry_category = self.entry_category.get().strip()
                if self.entry_subcategory.get() in ["None", ""]:
                    category = Category(entry_category)
                else:
                    entry_subcategory = self.entry_subcategory.get().strip()
                    category = Category(entry_category, entry_subcategory)

            temp_item = Item.create(
                self.entry_name.get(),
                float(self.entry_amount.get()),
                self.entry_description.get(),
                self.entry_date.get(),
                category,
            )
            return temp_item
        except ValueError as value_error:
            print(value_error)
            return None

    def on_row_selected(self, e):
        """Callback for row selection event."""

        # Reference: https://stackoverflow.com/questions/30614279/tkinter-treeview-get-selected-item-values

        # Reference: For Multiple Selected Rows
        # https://stackoverflow.com/questions/48867800/tk-treeview-focus-how-do-i-get-multiple-selected-lines

        # Set the Selected Item for the TreeView
        selected_item = self.items_table.focus()
        item_dct = self.items_table.item(selected_item)

        values = item_dct["values"]
        item_id = item_dct["text"]
        row = [item_id] + list(values)

        self.fill_form(
            values[0],
            values[1],
            values[2],
            values[3],
            category=values[4],
            subcategory=values[5],
        )


if __name__ == "__main__":
    DB_PATH = str(Path(__file__).resolve().parent / "items.json")
    app = App(DB_PATH)
    app.mainloop()
