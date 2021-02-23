import pandas as pd
from reconciler import reconcile


def reconcile_profs():

    profs = pd.read_csv("results/profs.csv")

    reconciled_profs = reconcile(profs["professor"], type_id="Q5")

    best_matches = reconciled_profs.loc[
        (reconciled_profs["score"].eq(100.0)) & (reconciled_profs["match"].eq(True))
    ][["id", "input_value"]]

    merged_profs = best_matches.merge(
        profs, left_on="input_value", right_on="professor", how="left"
    ).drop("input_value", axis=1)

    merged_profs["lattes_id"] = merged_profs["lattes"].str.replace(
        "http://lattes.cnpq.br/", "", regex=True
    )

    return merged_profs


def create_qs(reconciled_df):

    with open("results/professors.qs", "w") as qs:
        affiliation_ref = 'S854|"https://bioinfo.imd.ufrn.br/index.php?page=people"|S813|+2021-02-22T00:00:00Z/11'

        for _, row in reconciled_df.iterrows():

            affiliation = f"{row['id']}|P1416|Q105627005|"
            lattes = f"{row['id']}|P1007|\"{row['lattes_id']}\"|"
            lattes_ref = f"S854|\"{row['lattes']}\""

            affiliation_statement = f"{affiliation}{affiliation_ref}\n"
            lattes_statement = f"{lattes}{lattes_ref}\n"

            qs.write(f"{affiliation_statement}{lattes_statement}")


if __name__ == "__main__":

    reconciled_profs = reconcile_profs()
    reconciled_profs.to_csv("results/reconciled_profs.csv", index=False)

    create_qs(reconciled_profs)