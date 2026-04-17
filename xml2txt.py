<<<<<<< HEAD:scripts/xml2txt.py
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.utils import voc_xmls_to_yolo_txts

voc_xmls_to_yolo_txts('./SCUT-HEAD/labels/val/', './SCUT-HEAD/labels/val/')
=======
import os
from core.utils import voc_xmls_to_yolo_txts

voc_xmls_to_yolo_txts('./SCUT-HEAD/labels/val/', './SCUT-HEAD/labels/val/')
>>>>>>> 8d37e7ddf65286e5aaac98caeb75e0edc266015c:xml2txt.py
