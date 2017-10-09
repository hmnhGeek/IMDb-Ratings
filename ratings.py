import imdb_ratings
import argparse as ap

parser = ap.ArgumentParser()
parser.add_argument('lower_limit', type = float, help = "Enter the required ratings.")
parser.add_argument('upper_limit', type = float, help = "Enter the required ratings.")
args = parser.parse_args()

imdb_ratings.find_movies(args.lower_limit, args.upper_limit)
