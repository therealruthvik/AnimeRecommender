from src.dataloader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder

from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting to building the Pipeline.......")

        loader = AnimeDataLoader("data/anime_with_synopsis.csv", "data/anime_updated.csv")

        processed_csv = loader.load_and_process() 
        logger.info("Data loaded and Processed")

        vector_builder  = VectorStoreBuilder(processed_csv)
        vector_builder.build_and_save_vector_store()

        logger.info("Vector Store built succcessfully")

        logger.info("Pipeline build Sucessfully")
    except Exception as e:
        logger.info("Failed to execute pipeline",e)


if __name__ == "__main__":
    main()