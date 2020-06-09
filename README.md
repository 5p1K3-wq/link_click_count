# Link click count
The script shortens the link using the api of the [Bitly](https://bitly.com/) service and also shows the statistics 
of clicks on the user-specified short link.
The user enters a long link for example:

![](https://imgur.com/5ijcB4x.png)

The script will return a short link:

![](https://imgur.com/pwYa31C.png)

If the user provides a short link:

![](https://imgur.com/61Ci8SH.png)

In this case, the script will return the number of clicks on this link.

![](https://imgur.com/ZBxc8eJ.png)

## Getting started
### Manual instruction
1. **Clone the repository** 
`
git clone https://github.com/5p1K3-wq/link_click_count.git
`
2.  **Open directory**
`cd link_click_count/`
3.  **We start the setup script**
`python3 setup.py`
4.  **Specify the values for the following variables:**
    *   `ACCESS_TOKEN` - Api key for working with the service [Bitly](https://bitly.com/).
5.  **Run the script `python3 main.py`.**

![](https://dvmn.org/media/filer_public/ca/45/ca4595c7-f119-4ee7-9326-ed9089e0be41/bitly.gif)

## Built With
[python-dotenv 0.13.0](https://pypi.org/project/python-dotenv/) - It allows you to load environment variables from the 
.env file in the root directory
