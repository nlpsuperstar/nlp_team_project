import requests
from bs4 import BeautifulSoup 
import pandas as pd
import re
from time import strftime
from time import sleep
import os
import json
from typing import Dict, List, Optional, Union, cast

from env import github_token, github_username

REPOS = ['thedaviddias/Front-End-Checklist',
 'onevcat/Kingfisher',
 'FallibleInc/security-guide-for-developers',
 'tailwindlabs/tailwindcss',
 'codepath/android_guides',
 'github/fetch',
 'formulahendry/955.WLB',
 'ianstormtaylor/slate',
 'Kong/insomnia',
 'CymChad/BaseRecyclerViewAdapterHelper',
 'ggreer/the_silver_searcher',
 'ReactiveX/RxSwift',
 'SheetJS/sheetjs',
 'elastic/elasticsearch',
 'DrKLO/Telegram',
 'angular/material',
 't4t5/sweetalert',
 '1c7/chinese-independent-developer',
 'bayandin/awesome-awesomeness',
 'tauri-apps/tauri',
 'pypa/pipenv',
 'judasn/IntelliJ-IDEA-Tutorial',
 'valyala/fasthttp',
 'pjreddie/darknet',
 'Homebrew/homebrew-cask',
 'ReactiveCocoa/ReactiveCocoa',
 'eriklindernoren/ML-From-Scratch',
 'komeiji-satori/Dress',
 'carbon-app/carbon',
 'bregman-arie/devops-exercises',
 'hwdsl2/setup-ipsec-vpn',
 'taichi-dev/taichi',
 'michalsnik/aos',
 'dotnet/corefx',
 'LingCoder/OnJava8',
 'elsewhencode/project-guidelines',
 'keon/algorithms',
 'zhaoolee/ChromeAppHeroes',
 'viatsko/awesome-vscode',
 'swagger-api/swagger-ui',
 'doocs/advanced-java',
 'iview/iview',
 'denysdovhan/wtfjs',
 'dotnet-architecture/eShopOnContainers',
 'ShareX/ShareX',
 'airyland/vux',
 'typicode/json-server',
 'spf13/viper',
 'libgdx/libgdx',
 'videojs/video.js',
 'avajs/ava',
 'Semantic-Org/Semantic-UI',
 'pandas-dev/pandas',
 'google/material-design-icons',
 'android/architecture-components-samples',
 'react-hook-form/react-hook-form',
 'PKUanonym/REKCARC-TSC-UHT',
 'apache/superset',
 'ossrs/srs',
 'CMU-Perceptual-Computing-Lab/openpose',
 'luong-komorebi/Awesome-Linux-Software',
 'terryum/awesome-deep-learning-papers',
 'sqlmapproject/sqlmap',
 'yuzu-emu/yuzu',
 'hoppscotch/hoppscotch',
 'HeroTransitions/Hero',
 'framework7io/framework7',
 'Modernizr/Modernizr',
 'bvaughn/react-virtualized',
 'dotnet/aspnetcore',
 'crystal-lang/crystal',
 'guzzle/guzzle',
 'amix/vimrc',
 'mxgmn/WaveFunctionCollapse',
 'byoungd/English-level-up-tips-for-Chinese',
 'SpaceVim/SpaceVim',
 'IanLunn/Hover',
 'greenrobot/EventBus',
 'wsargent/docker-cheat-sheet',
 'ascoders/weekly',
 'DopplerHQ/awesome-interview-questions',
 'tmux/tmux',
 'realpython/python-guide',
 'tabler/tabler',
 'conwnet/github1s',
 'nektos/act',
 'alibaba/ice',
 'prettier/prettier',
 'goldfire/howler.js',
 'ReactiveX/RxJava',
 'facebook/rocksdb',
 'nylas/nylas-mail',
 'FFmpeg/FFmpeg',
 'wagoodman/dive',
 'neovim/neovim',
 'halfrost/LeetCode-Go',
 'mpv-player/mpv',
 'didi/DoraemonKit',
 'minimaxir/big-list-of-naughty-strings',
 'herrbischoff/awesome-macos-command-line',
 'rust-lang/rust',
 'Netflix/Hystrix',
 'hammerjs/hammer.js',
 'Dreamacro/clash',
 'quilljs/quill',
 'rails/rails',
 'vapor/vapor',
 'ovity/octotree',
 'signalapp/Signal-Android',
 'zsh-users/zsh-autosuggestions',
 'scrapy/scrapy',
 'google/iosched',
 'Baseflow/PhotoView',
 'netdata/netdata',
 'mtdvio/every-programmer-should-know',
 'unknwon/the-way-to-go_ZH_CN',
 'blueimp/jQuery-File-Upload',
 'sebastianruder/NLP-progress',
 'harvesthq/chosen',
 'kelseyhightower/nocode',
 'cdr/code-server',
 'codemirror/CodeMirror',
 'facebook/hhvm',
 'philc/vimium',
 'zyedidia/micro',
 'libuv/libuv',
 'microsoft/api-guidelines',
 'django/django',
 'beurtschipper/Depix',
 'jakevdp/PythonDataScienceHandbook',
 'webtorrent/webtorrent',
 'sherlock-project/sherlock',
 'afollestad/material-dialogs',
 'tonsky/FiraCode',
 'chenglou/react-motion',
 'ElemeFE/mint-ui',
 'redisson/redisson',
 'jamiebuilds/the-super-tiny-compiler',
 'danielgindi/Charts',
 'fxsjy/jieba',
 'DesignPatternsPHP/DesignPatternsPHP',
 'shadowsocks/shadowsocks-android',
 'google-research/bert',
 'rstacruz/nprogress',
 'vuejs/awesome-vue',
 'angular/components',
 'pallets/flask',
 'gorhill/uBlock',
 'rancher/rancher',
 'webpack/webpack',
 'niklasvh/html2canvas',
 'vnpy/vnpy',
 'sindresorhus/quick-look-plugins',
 'evanw/esbuild',
 'matteocrippa/awesome-swift',
 'angular/angular-cli',
 'hashicorp/vagrant',
 'trailofbits/algo',
 'facebook/flow',
 'VincentGarreau/particles.js',
 'nefe/You-Dont-Need-jQuery',
 'apache/kafka',
 'typescript-cheatsheets/react',
 'cmderdev/cmder',
 'labstack/echo',
 'nlohmann/json',
 'cheeriojs/cheerio',
 'alpinejs/alpine',
 'MostlyAdequate/mostly-adequate-guide',
 'hashicorp/consul',
 'getsentry/sentry',
 'bilibili/flv.js',
 'square/leakcanary',
 'basecamp/trix',
 'SwiftyJSON/SwiftyJSON',
 'mozilla/DeepSpeech',
 'Automattic/mongoose',
 'caolan/async',
 'Binaryify/NeteaseCloudMusicApi',
 'taosdata/TDengine',
 'react-boilerplate/react-boilerplate',
 'swisskyrepo/PayloadsAllTheThings',
 'markedjs/marked',
 'yarnpkg/yarn',
 'elixir-lang/elixir',
 'sirupsen/logrus',
 'mojs/mojs',
 'TheAlgorithms/C-Plus-Plus',
 'standard/standard',
 'iperov/DeepFaceLab',
 'Meituan-Dianping/mpvue',
 'rome/tools',
 'serverless/serverless',
 'azl397985856/leetcode',
 'mobxjs/mobx',
 'StevenBlack/hosts',
 'eslint/eslint',
 'numpy/numpy',
 'rclone/rclone',
 'babel/babel',
 'rwaldron/idiomatic.js',
 'ApolloAuto/apollo',
 'Hack-with-Github/Awesome-Hacking',
 'graphql/graphql-js',
 'nushell/nushell',
 'adam-golab/react-developer-roadmap',
 'encode/django-rest-framework',
 'google-research/google-research',
 'ray-project/ray',
 'GeekyAnts/NativeBase',
 'GoogleChrome/lighthouse',
 'leonardomso/33-js-concepts',
 'Polymer/polymer',
 'tj/commander.js',
 'microsoft/monaco-editor',
 'google/gson',
 'halo-dev/halo',
 'microsoft/calculator',
 'meteor/meteor',
 'BurntSushi/ripgrep',
 'akveo/ngx-admin',
 'meilisearch/MeiliSearch',
 'jtoy/awesome-tensorflow',
 'microsoft/PowerToys',
 'markerikson/react-redux-links',
 'alibaba/canal',
 'winstonjs/winston',
 'elastic/kibana',
 'facebook/flux',
 'tipsy/profile-summary-for-github',
 'julianshapiro/velocity',
 'tmrts/go-patterns',
 'balderdashy/sails',
 'verekia/js-stack-from-scratch',
 'chubin/cheat.sh',
 'wenyan-lang/wenyan',
 'sharkdp/fd',
 'immutable-js/immutable-js',
 'google/zx',
 'processing/p5.js',
 'aymericdamien/TensorFlow-Examples',
 'hasura/graphql-engine',
 'facebookresearch/fastText',
 'airbnb/lottie-ios',
 'MustangYM/WeChatExtension-ForMac',
 'transloadit/uppy',
 'lutzroeder/netron',
 'sindresorhus/awesome-nodejs',
 'spf13/cobra',
 'gofiber/fiber',
 'iina/iina',
 'kamranahmedse/design-patterns-for-humans',
 'yangshun/tech-interview-handbook',
 'eugeneyan/applied-ml',
 'dkhamsing/open-source-ios-apps',
 'reactnativecn/react-native-guide',
 'cockroachdb/cockroach',
 'magenta/magenta',
 'ibraheemdev/modern-unix',
 'alibaba/arthas',
 'dokku/dokku',
 'strapi/strapi',
 'huihut/interview',
 'littlecodersh/ItChat',
 'dbeaver/dbeaver',
 'zhiwehu/Python-programming-exercises',
 'starship/starship',
 'poteto/hiring-without-whiteboards',
 'mdbootstrap/mdb-ui-kit',
 'dnSpy/dnSpy',
 'reduxjs/redux',
 'jesseduffield/lazygit',
 'haizlin/fe-interview',
 'python-poetry/poetry',
 '0xAX/linux-insides',
 'vuejs/devtools',
 'psf/black',
 'segmentio/nightmare',
 'jekyll/jekyll',
 'istio/istio',
 'neoclide/coc.nvim',
 'papers-we-love/papers-we-love',
 'websockets/ws',
 'BVLC/caffe',
 'grafana/grafana',
 'tannerlinsley/react-query',
 'lenve/vhr',
 'ftlabs/fastclick',
 'highlightjs/highlight.js',
 'dwmkerr/hacker-laws',
 'ruanyf/weekly',
 'svg/svgo',
 'agalwood/Motrix',
 'faif/python-patterns',
 'certbot/certbot',
 'alibaba/fastjson',
 'isocpp/CppCoreGuidelines',
 'remix-run/react-router',
 'reduxjs/react-redux',
 'Genymobile/scrcpy',
 'portainer/portainer',
 'select2/select2',
 '521xueweihan/HelloGitHub',
 'seata/seata',
 'NationalSecurityAgency/ghidra',
 'postcss/autoprefixer',
 'nocodb/nocodb',
 'vuejs/vuepress',
 'handlebars-lang/handlebars.js',
 'Advanced-Frontend/Daily-Interview-Question',
 'swc-project/swc',
 'typicode/husky',
 'ColorlibHQ/gentelella',
 'google/flexbox-layout',
 'kelthuzadx/hosts',
 'elunez/eladmin',
 'jgraph/drawio',
 'jenkinsci/jenkins',
 'scikit-learn/scikit-learn',
 'SwiftGGTeam/the-swift-programming-language-in-chinese',
 'practical-tutorials/project-based-learning',
 'SnapKit/Masonry',
 'urfave/cli',
 'vuejs/vue-next',
 'bazelbuild/bazel',
 'sebastianbergmann/phpunit',
 'jamiebuilds/react-loadable',
 'JakeWharton/butterknife',
 'fabricjs/fabric.js',
 'davideuler/architecture.of.internet-product',
 'go-delve/delve',
 'syl20bnr/spacemacs',
 'lib-pku/libpku',
 'pbatard/rufus',
 'inconshreveable/ngrok',
 'prisma/prisma',
 'vercel/pkg',
 'rethinkdb/rethinkdb',
 'apollographql/apollo-client',
 'facebookresearch/detectron2',
 'parse-community/parse-server',
 'defunkt/jquery-pjax',
 'naptha/tesseract.js',
 'hollischuang/toBeTopJavaer',
 'HelloZeroNet/ZeroNet',
 'SnapKit/SnapKit',
 'docsifyjs/docsify',
 'geekcompany/ResumeSample',
 'facebookresearch/Detectron',
 'ventoy/Ventoy',
 'juliangarnier/anime',
 'CSSEGISandData/COVID-19',
 'mastodon/mastodon',
 'chartjs/Chart.js',
 'tastejs/todomvc',
 'zenorocha/clipboard.js',
 'crossoverJie/JCSprout',
 'necolas/react-native-web',
 'typicode/lowdb',
 'geekcomputers/Python',
 'nvbn/thefuck',
 'sahat/hackathon-starter',
 'bannedbook/fanqiang',
 'jhipster/generator-jhipster',
 'ehang-io/nps',
 'celery/celery',
 'kenwheeler/slick',
 'linlinjava/litemall',
 'MLEveryday/100-Days-Of-ML-Code',
 'donnemartin/data-science-ipython-notebooks',
 'bevacqua/dragula',
 'ultralytics/yolov5',
 'kataras/iris',
 'SDWebImage/SDWebImage',
 'python/cpython',
 '2dust/v2rayN',
 'StreisandEffect/streisand',
 'serhii-londar/open-source-mac-os-apps',
 'jgraph/drawio-desktop',
 'ColorlibHQ/AdminLTE',
 'alebcay/awesome-shell',
 'iptv-org/iptv',
 'wekan/wekan',
 'apache/flink',
 'hashicorp/vault',
 'alibaba/druid',
 'kon9chunkit/GitHub-Chinese-Top-Charts',
 'satwikkansal/wtfpython',
 'fouber/blog',
 'Fndroid/clash_for_windows_pkg',
 'microsoft/CNTK',
 'uikit/uikit',
 'alibaba/flutter-go',
 'topjohnwu/Magisk',
 'JedWatson/react-select',
 'Awesome-HarmonyOS/HarmonyOS',
 'uglide/RedisDesktopManager',
 'academic/awesome-datascience',
 'xi-editor/xi-editor',
 'jgthms/bulma',
 'js-cookie/js-cookie',
 'houshanren/hangzhou_house_knowledge',
 'apache/skywalking',
 'mbeaudru/modern-js-cheatsheet',
 'syncthing/syncthing',
 'angular/angular.js',
 'freeCodeCamp/devdocs',
 'kriasoft/react-starter-kit',
 'zxing/zxing',
 'bitcoin/bitcoin',
 'grpc/grpc',
 'lukasz-madon/awesome-remote-job',
 'fengdu78/Coursera-ML-AndrewNg-Notes',
 'n0shake/Public-APIs',
 'SortableJS/Sortable',
 'netty/netty',
 'fish-shell/fish-shell',
 'alsotang/node-lessons',
 'kubernetes/minikube',
 'facebook/docusaurus',
 'facebook/draft-js',
 'Wox-launcher/Wox',
 'jsdom/jsdom',
 'eggjs/egg',
 'notable/notable',
 'immerjs/immer',
 'swoole/swoole-src',
 'bumptech/glide',
 'dracula/dracula-theme',
 'Homebrew/legacy-homebrew',
 'qiurunze123/miaosha',
 'composer/composer',
 'dromara/hutool',
 'VundleVim/Vundle.vim',
 'adobe-fonts/source-code-pro',
 'supabase/supabase',
 'remoteintech/remote-jobs',
 'ajaxorg/ace',
 'junegunn/fzf',
 'dylanaraps/pure-bash-bible',
 'jaredhanson/passport',
 'datawhalechina/pumpkin-book',
 'phoenixframework/phoenix',
 'spring-projects/spring-boot',
 'explosion/spaCy',
 'coolsnowwolf/lede',
 'date-fns/date-fns',
 'opencv/opencv',
 'koalaman/shellcheck',
 'BoostIO/BoostNote-Legacy',
 'apache/echarts',
 'google/eng-practices',
 'doczjs/docz',
 'codex-team/editor.js',
 'vuejs/vuex',
 'pyenv/pyenv',
 'pcottle/learnGitBranching',
 'yewstack/yew',
 'hankcs/HanLP',
 'CodeHubApp/CodeHub',
 'beego/beego',
 'AobingJava/JavaFamily',
 'nagadomi/waifu2x',
 'skylot/jadx',
 'yunjey/pytorch-tutorial',
 'junegunn/vim-plug',
 'alibaba/Sentinel',
 'wesbos/JavaScript30',
 'railsware/upterm',
 'gfwlist/gfwlist',
 'mitmproxy/mitmproxy',
 'atom/atom',
 'felixrieseberg/windows95',
 'ycm-core/YouCompleteMe',
 'bitcoinbook/bitcoinbook',
 'homebridge/homebridge',
 'youngyangyang04/leetcode-master',
 'microsoft/ML-For-Beginners',
 'powerline/fonts',
 'jquery/jquery',
 'home-assistant/core',
 'moby/moby',
 'spring-projects/spring-framework',
 'Leaflet/Leaflet',
 'forem/forem',
 'parallax/jsPDF',
 'reduxjs/reselect',
 'alex/what-happens-when',
 'react-dnd/react-dnd',
 'DIYgod/RSSHub',
 'sindresorhus/awesome-electron',
 'eugenp/tutorials',
 'square/okhttp',
 'vim/vim',
 'SortableJS/Vue.Draggable',
 'php/php-src',
 'influxdata/influxdb',
 'jcjohnson/neural-style',
 'gitlabhq/gitlabhq',
 'apple/swift',
 'nicolargo/glances',
 'shengxinjing/programmer-job-blacklist',
 'git/git',
 'apache/airflow',
 'fastify/fastify',
 'wuyouzhuguli/SpringAll',
 'foundation/foundation-sites',
 'jorgebucaran/hyperapp',
 'aria2/aria2',
 'n8n-io/n8n',
 'mathiasbynens/dotfiles',
 'YMFE/yapi',
 'ClickHouse/ClickHouse',
 'facebook/fresco',
 'hakimel/reveal.js',
 'snowpackjs/snowpack',
 'gothinkster/realworld',
 'openai/gym',
 'pingcap/tidb',
 'docker/compose',
 'nestjs/nest',
 'yeasy/docker_practice',
 'servo/servo',
 'curl/curl',
 'ryanhanwu/How-To-Ask-Questions-The-Smart-Way',
 'Pierian-Data/Complete-Python-3-Bootcamp',
 'reduxjs/redux-thunk',
 'google/python-fire',
 'OWASP/CheatSheetSeries',
 'mqyqingfeng/Blog',
 'schollz/croc',
 'golang-standards/project-layout',
 'sdras/awesome-actions',
 'dimsemenov/PhotoSwipe',
 'chakra-ui/chakra-ui',
 'AllThingsSmitty/css-protips',
 'ccxt/ccxt',
 'OAI/OpenAPI-Specification',
 'mochajs/mocha',
 'less/less.js',
 'facebook/folly',
 'osquery/osquery',
 'robertdavidgraham/masscan',
 'brillout/awesome-react-components',
 'jashkenas/backbone',
 'Seldaek/monolog',
 'locustio/locust',
 'ryanmcdermott/clean-code-javascript',
 'ionic-team/ionic-framework',
 'gohugoio/hugo',
 'soimort/you-get',
 'TheAlgorithms/Java',
 'alibaba/p3c',
 'nothings/stb',
 'wasabeef/awesome-android-ui',
 'tornadoweb/tornado',
 'emscripten-core/emscripten',
 'gulpjs/gulp',
 'alibaba/weex',
 'dmlc/xgboost']

headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}

if headers["Authorization"] == "token " or headers["User-Agent"] == "":
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it"
    )


def github_api_request(url: str) -> Union[List, Dict]:
    response = requests.get(url, headers=headers)
    response_data = response.json()
    if response.status_code != 200:
        raise Exception(
            f"Error response from github api! status code: {response.status_code}, "
            f"response: {json.dumps(response_data)}"
        )
    return response_data


def get_repo_language(repo: str) -> str:
    url = f"https://api.github.com/repos/{repo}"
    repo_info = github_api_request(url)
    if type(repo_info) is dict:
        repo_info = cast(Dict, repo_info)
        if "language" not in repo_info:
            raise Exception(
                "'language' key not round in response\n{}".format(json.dumps(repo_info))
            )
        return repo_info["language"]
    raise Exception(
        f"Expecting a dictionary response from {url}, instead got {json.dumps(repo_info)}"
    )


def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo}/contents/"
    contents = github_api_request(url)
    if type(contents) is list:
        contents = cast(List, contents)
        return contents
    raise Exception(
        f"Expecting a list response from {url}, instead got {json.dumps(contents)}"
    )


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api that lists the files in a repo and
    returns the url that can be used to download the repo's README file.
    """
    for file in files:
        if file["name"].lower().startswith("readme"):
            return file["download_url"]
    return ""


def process_repo(repo: str) -> Dict[str, str]:
    """
    Takes a repo name like "gocodeup/codeup-setup-script" and returns a
    dictionary with the language of the repo and the readme contents.
    """
    contents = get_repo_contents(repo)
    readme_download_url = get_readme_download_url(contents)
    if readme_download_url == "":
        readme_contents = ""
    else:
        readme_contents = requests.get(readme_download_url).text
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": readme_contents,
    }


def scrape_github_data() -> List[Dict[str, str]]:
    """
    Loop through all of the repos and process them. Returns the processed data.
    """
    return [process_repo(repo) for repo in REPOS]


if __name__ == "__main__":
    data = scrape_github_data()
    json.dump(data, open("data.json", "w"), indent=1)