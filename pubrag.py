import chromadb
import pandas as pd
import glob




def create_vector_store(pubmed_data_folder, chroma_folder):
    """ """

    # init collection
    chroma_client = chromadb.Client()
    collection = chroma_client.create_collection(name="pubmed")

    # load documents
    for pubmed_file in glob.glob(f"{pubmed_data_folder}/*.parquet"):

        document_list = []
        metadatas = []
        ids = []
        df = pd.read_parquet(pubmed_file)
        for index, row in df.iterrows():

            # extract infos
            text = f"{row['TITLE']}. {row['ABSTRACT']}"
            pmid = row['PMID']
            publication_date = row['DATE']
            journal = row['JOURNAL']
            journal_country = row['JOURNAL_COUNTRY']
            article_type = row['TYPE']
            article_language = row['LANGUAGE']
            mesh = row['MESH']
            mesh_id = row['MESH_ID']
            chem = row['CHEM']
            chem_id = row['CHEM_ID']
            authors = row['AUTHORS']

            # forge data to add
            document_list.append(text)
            metadatas.append({"PMID":pmid,
                             "DATE":publication_date,
                             "JOURNAL":journal,
                             "JOURNAL_COUNTRY":journal_country,
                             "TYPE":article_type,
                             "LANGUAGE":article_language,
                             "MESH":mesh,
                             "MESH_ID":mesh_id,
                             "CHEM":chem,
                             "CHEM_ID":chem_id,
                             "AUTHORS":authors
                         })
            ids.append(pmid)

        # add document to collection
        collection.add(
            documents=document_list,
            metadatas=metadatas,
            ids=ids
        )


            




if __name__ == "__main__":


    # parameters
    pubmed_data_folder = "/home/n765/data/pubmed"
    chroma_folder = "/home/n765/data/chroma_db"

    # run function
    create_vector_store(pubmed_data_folder, chroma_folder)


