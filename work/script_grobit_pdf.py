from grobid_client_python.grobid_client.grobid_client import GrobidClient

client = GrobidClient(config_path="../grobid_client_python/config.json")
client.process("processFulltextDocument",  "./dataset", output="./output/", tei_coordinates=True, force=True)
