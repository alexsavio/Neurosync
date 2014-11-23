
import os
import os.path as op
from   glob    import glob
import logging

from   neurosync.utils.rcfile   import rcfile
from   neurosync.utils.matfiles import loadmat

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


if __name__ == '__main__':

    settings = rcfile('miren_negation')
    segs_dir = settings['segments_dir']

    log.info('Reading data from {}'.format(segs_dir))
    subj_files = glob(op.join(segs_dir, '*.set'))

    data = loadmat(subj_files[0])['EEG']

    # channel localizations
    data['chanlocs']
