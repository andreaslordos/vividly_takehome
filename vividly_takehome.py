import os
import argparse
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

def download_files(args):
    if args.save_here:
        save_path = os.getcwd()
    else:
        save_path = args.save_path
        if not os.path.exists(args.save_path):
            os.mkdir(args.save_path)
    print("Set folder: {}".format(save_path))
    print("Fetching site...")
    response = requests.get(args.link, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'})
    soup = BeautifulSoup(response.text, "html.parser")
    pdf_list = soup.select(f"a[href$='.{args.filetype}']") # list of pdfs and their links, <a href="/wp-content/uploads/2019/07/exam1969.pdf">Problem Set</a>
    print("{} files found".format(len(pdf_list)))
    print("Starting to download...")
    for counter, link in enumerate(pdf_list):
        filename = link['href'].split('/')[-1] # in above example filename would be exam1969.pdf
        file_save_path = os.path.join(save_path,filename) 
        if not args.quiet:
            print("[{}/{}] {}".format(counter+1, len(pdf_list), filename)) # print counter to show progress
        with open(file_save_path, 'wb') as f:
            f.write(requests.get(urljoin(args.link,link['href'])).content) # fetch pdf and write to file
    print("Download complete")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Argparse for file downloader')
    
    # Options
    # -l/--link
    # required
    parser.add_argument('-l', '--link', required=True, type=str,
                        help='Site URL to scrape')
    
    # --filetype
    # default: pdf
    parser.add_argument('-ft', '--filetype', dest='filetype', type=str,
                        help="Set filetype to download")
    parser.set_defaults(filetype="pdf")
    

    # --quiet
    # default: False
    parser.add_argument('--quiet', dest='quiet', action='store_true',
                        help="Quiet mode; don't print filenames")
    parser.set_defaults(quiet=False)
    
    # --save-here
    # default: False
    parser.add_argument('--save-here', dest='save_here', action='store_true',
                        help="Save files in current directory")
    parser.set_defaults(save_here=False)
    
    # --save-path
    # default: Downloads
    parser.add_argument('-f', '--save-path', default=r""+os.path.join(os.path.expanduser('~'), "Downloads"), 
                        type=str, help='Save files in the provided folder')
    
    args = parser.parse_args()
    download_files(args)