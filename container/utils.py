# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import google.cloud.logging
import logging
import os

if not os.environ.get('RUN_LOCALLY'):
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    client = google.cloud.logging.Client()
    client.setup_logging()              
    logger = client.logger('scraper')
else:
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    logger = logging.Logger('scraper')

def logText(text):
    if not os.environ.get('RUN_LOCALLY'):
       logger.log_text(text)
    else:
       print(text)