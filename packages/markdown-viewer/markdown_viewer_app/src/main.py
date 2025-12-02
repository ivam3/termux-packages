import flet as ft
import os
import re

# Construir una ruta absoluta al directorio de assets y mds para que sea robusto
APP_DIR = os.path.dirname(os.path.abspath(__file__))
MDS_PATH = os.path.join(APP_DIR, "storage", "mds")

def main(page: ft.Page):
    page.title = "Ivam3byCinderella - Markdown Viewer"
    page.window_width = 900
    page.window_height = 700
    page.theme = ft.Theme(color_scheme_seed="blue")
    page.padding = 0

    all_md_files = []
    original_md_content = ""

    # --- Refs para acceder a los controles ---
    files_list_ref = ft.Ref[ft.Column]()
    md_view_ref = ft.Ref[ft.Markdown]()
    search_text_ref = ft.Ref[ft.TextField]()
    status_text_ref = ft.Ref[ft.Text]()
    left_panel_ref = ft.Ref[ft.Container]()

    def load_markdown_files():
        if os.path.exists(MDS_PATH):
            for file in os.listdir(MDS_PATH):
                if file.endswith(".md"):
                    all_md_files.append(file)
            all_md_files.sort()

    def open_markdown_file(e):
        nonlocal original_md_content
        file_path = os.path.join(MDS_PATH, e.control.data)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                original_md_content = f.read()
            
            if search_text_ref.current: search_text_ref.current.value = ""
            if md_view_ref.current:
                md_view_ref.current.value = original_md_content
                md_view_ref.current.update()
        except Exception as ex:
            original_md_content = f"Error al abrir el archivo: {ex}"
            if md_view_ref.current:
                md_view_ref.current.value = original_md_content
                md_view_ref.current.update()

    def update_file_list(search_term=""):
        if files_list_ref.current is None: return
        filtered_files = [f for f in all_md_files if search_term.lower() in f.lower()]
        files_list_ref.current.controls.clear()
        for file_name in filtered_files:
            files_list_ref.current.controls.append(
                ft.ListTile(
                    title=ft.Text(file_name, max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
                    data=file_name, on_click=open_markdown_file, leading=ft.Icon(ft.Icons.DESCRIPTION), height=40,
                )
            )
        files_list_ref.current.update()

    def search_files(e): update_file_list(e.control.value)

    def search_in_file(e):
        search_term = e.control.value
        if not search_term or not md_view_ref.current:
            md_view_ref.current.value = original_md_content
        else:
            highlighted_content = re.sub(
                f"({re.escape(search_term)})", r"<mark>\1</mark>", original_md_content, flags=re.IGNORECASE
            )
            md_view_ref.current.value = highlighted_content
        md_view_ref.current.update()
        
    def on_pan_resize(e: ft.DragUpdateEvent):
        """Manejador para redimensionar el panel izquierdo."""
        if left_panel_ref.current:
            new_width = left_panel_ref.current.width + e.delta_x
            if 150 <= new_width <= 500:
                left_panel_ref.current.width = new_width
                left_panel_ref.current.update()

    # --- Definición de la UI ---
    file_search_field = ft.TextField(
        label="Buscar archivo...", on_change=search_files, prefix_icon=ft.Icons.SEARCH, border_radius=20,
    )
    text_search_field = ft.TextField(
        ref=search_text_ref, label="Buscar en el texto...", on_change=search_in_file,
        prefix_icon=ft.Icons.FIND_IN_PAGE, border_radius=20, expand=True,
    )

    left_panel = ft.Container(
        ref=left_panel_ref,
        content=ft.Column(
            [
                ft.Text("Archivos", style=ft.TextThemeStyle.HEADLINE_SMALL, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                file_search_field,
                ft.Text(ref=status_text_ref, size=10, color=ft.Colors.WHITE70, text_align=ft.TextAlign.CENTER),
                ft.Column(ref=files_list_ref, scroll=ft.ScrollMode.ADAPTIVE, expand=True),
            ],
            spacing=5, horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
        ),
        width=270, bgcolor=ft.Colors.BLUE_GREY_900,
        padding=10, border_radius=ft.border_radius.only(top_right=8, bottom_right=8),
    )

    right_panel = ft.Column(
        [
            ft.Row([text_search_field]),
            ft.Column(
                [ft.Markdown(
                    ref=md_view_ref, value="**Selecciona un archivo** para ver su contenido.", selectable=True,
                    extension_set=ft.MarkdownExtensionSet.GITHUB_WEB, on_tap_link=lambda e: page.launch_url(e.data),
                )],
                expand=True, scroll=ft.ScrollMode.ADAPTIVE,
            )
        ],
        expand=True, spacing=10,
    )
    
    # --- Lógica de Arranque ---
    page.add(
        ft.Row(
            [
                left_panel,
                ft.GestureDetector(
                    content=ft.VerticalDivider(),
                    on_pan_update=on_pan_resize,
                    mouse_cursor=ft.MouseCursor.RESIZE_LEFT_RIGHT,
                ),
                right_panel,
            ],
            expand=True, spacing=0,
        )
    )

    load_markdown_files()
    if status_text_ref.current:
        status_text_ref.current.value = f"{len(all_md_files)} archivos encontrados." if os.path.exists(MDS_PATH) else "Directorio NO encontrado."
        status_text_ref.current.update()
    update_file_list()
    page.update()

if __name__ == "__main__":
    ft.app(target=main, assets_dir=os.path.join(APP_DIR, "assets"))
