from config import SAVING_TABLE, SCALED_ENCONDING_TABLE
import pandas as pd


def upsert_saving(cursor, df_saving):
    df_saving = df_saving[df_saving["product_id"].notna()]
    for _, row in df_saving.iterrows():
        # Chuyển NaN -> None
        row_data = {k: (None if pd.isna(v) else v) for k, v in row.items()}

        # Kiểm tra tồn tại
        cursor.execute(f"SELECT 1 FROM {SCALED_ENCONDING_TABLE} WHERE product_id=?", row_data["product_id"])
        exists = cursor.fetchone()

        if exists:
            cursor.execute(f"""
                UPDATE {SCALED_ENCONDING_TABLE}
                SET brand=?, os=?, ram=?, rom=?, battery=?,
                    camera_primary=?, camera_secondary=?, chipset=?, gpu=?,
                    display_size=?, screen=?, sensor=?,
                    watt=?, nfc=?, jack_support=?, price=?
                WHERE product_id=?
            """, (
                row_data["brand"], row_data["os"], row_data["ram"], row_data["rom"],
                row_data["battery"], row_data["camera_primary"], row_data["camera_secondary"],
                row_data["chipset"], row_data["gpu"],
                row_data["display_size"], row_data["screen"], row_data["sensor"], row_data["watt"],
                row_data["nfc"], row_data["jack_support"], row_data["price"],
                row_data["product_id"]
            ))
        else:
            cursor.execute(f"""
                INSERT INTO {SCALED_ENCONDING_TABLE} (
                    product_id, brand, os, ram, rom, battery,
                    camera_primary, camera_secondary, chipset, gpu,
                    display_size, screen, sensor,
                    watt, nfc, jack_support, price
                )
                VALUES (
                        ?, ?, ?, ?, ?, ?, ?, ?, 
                        ?, ?, ?, ?, ?, ?, ?, ?, ?
                    )

            """, (
                row_data["product_id"], row_data["brand"], row_data["os"],
                row_data["ram"], row_data["rom"], row_data["battery"],
                row_data["camera_primary"], row_data["camera_secondary"], row_data["chipset"],
                row_data["gpu"], row_data["display_size"],
                row_data["screen"], row_data["sensor"], row_data["watt"], row_data["nfc"],
                row_data["jack_support"], row_data["price"]
            ))
