from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import CrawlerItem


class CrawlerSpider(Spider):
    name = "crawler"
    allowed_domains = ["sanfoundry.com"]
    start_urls = [
        "https://www.sanfoundry.com/operating-system-questions-answers-basics/",
        "https://www.sanfoundry.com/operating-system-questions-answers-processes/",
        "https://www.sanfoundry.com/operating-system-mcqs-process-control-block/",
        "https://www.sanfoundry.com/operating-system-mcqs-process-scheduling-queue/",
        "https://www.sanfoundry.com/operating-system-questions-answers-process-synchronization/",
        "https://www.sanfoundry.com/operating-system-mcqs-process-creation/",
        "https://www.sanfoundry.com/operating-system-mcqs-inter-process-communication/",
        "https://www.sanfoundry.com/operating-system-mcqs-process-rpc/",
        "https://www.sanfoundry.com/operating-system-mcqs-process-structures/",
        "https://www.sanfoundry.com/operating-system-questions-answers-cpu-scheduling/",
        "https://www.sanfoundry.com/operating-system-mcqs-cpu-scheduling-benefits/",
        "https://www.sanfoundry.com/operating-system-mcqs-cpu-scheduling-algorithms-1/",
        "https://www.sanfoundry.com/operating-system-mcqs-cpu-scheduling-algorithms-2/",
        "https://www.sanfoundry.com/operating-system-mcqs-critical-section-problem/",
        "https://www.sanfoundry.com/operating-system-mcqs-semaphores-1/",
        "https://www.sanfoundry.com/operating-system-mcqs-semaphores-2/",
        "https://www.sanfoundry.com/operating-system-mcqs-classic-sync-problems/",
        "https://www.sanfoundry.com/operating-system-mcqs-process-sync-monitors/",
        "https://www.sanfoundry.com/operating-system-mcqs-atomic-transactions/",
        "https://www.sanfoundry.com/operating-system-questions-answers-deadlock/",
        "https://www.sanfoundry.com/operating-system-mcqs-deadlock-prevention/",
        "https://www.sanfoundry.com/operating-system-mcqs-deadlock-avoidance/",
        "https://www.sanfoundry.com/operating-system-mcqs-deadlock-detection/",
        "https://www.sanfoundry.com/operating-system-mcqs-deadlock-recovery/",
        "https://www.sanfoundry.com/operating-system-mcqs-memory-management-swapping-1/",
        "https://www.sanfoundry.com/operating-system-mcqs-memory-management-swapping-2/",
        "https://www.sanfoundry.com/operating-system-questions-answers-memory-management/",
        "https://www.sanfoundry.com/operating-system-mcqs-memory-allocation-1/",
        "https://www.sanfoundry.com/operating-system-mcqs-memory-allocation-2/",
        "https://www.sanfoundry.com/operating-system-mcqs-memory-management-paging-1/",
        "https://www.sanfoundry.com/operating-system-mcqs-memory-management-paging-2/",
        "https://www.sanfoundry.com/operating-system-mcqs-memory-management-segmentation/",
        "https://www.sanfoundry.com/operating-system-mcqs-application-io-interface-1/",
        "https://www.sanfoundry.com/operating-system-mcqs-application-io-interface-2/",
        "https://www.sanfoundry.com/operating-system-mcqs-kernel-io-subsystems/",
        "https://www.sanfoundry.com/operating-system-questions-answers-rtos/",
        "https://www.sanfoundry.com/realtime-operating-system-mcqs-1/",
        "https://www.sanfoundry.com/realtime-operating-system-mcqs-2/",
        "https://www.sanfoundry.com/realtime-operating-system-mcqs-CPU-scheduling-1/",
        "https://www.sanfoundry.com/realtime-operating-system-mcqs-CPU-scheduling-2/",
        "https://www.sanfoundry.com/operating-system-question-answers-multimedia-systems/",
        "https://www.sanfoundry.com/operating-system-mcqs-multimedia-system-compression-1/",
        "https://www.sanfoundry.com/operating-system-mcqs-multimedia-system-compression-2/",
        "https://www.sanfoundry.com/operating-system-mcqs-multimedia-system-compression-3/",
        "https://www.sanfoundry.com/operating-system-mcqs-multimedia-system-CPU-disk-scheduling/",
        "https://www.sanfoundry.com/operating-system-mcqs-multimedia-system-network-management/",
        "https://www.sanfoundry.com/operating-system-mcqs-security-user-authentication/",
        "https://www.sanfoundry.com/operating-system-mcqs-security-program-system-threats/",
        "https://www.sanfoundry.com/operating-system-mcqs-security-system-facility/",
        "https://www.sanfoundry.com/operating-system-mcqs-security-intrusion-detection/",
        "https://www.sanfoundry.com/operating-system-mcqs-security-cryptography/",
        "https://www.sanfoundry.com/operating-system-questions-answers-secondary-storage/",
        "https://www.sanfoundry.com/operating-system-questions-answers-linux/",
        "https://www.sanfoundry.com/operating-system-questions-answers-threads/",
        "https://www.sanfoundry.com/operating-system-mcqs-threads-ult-klt/",
        "https://www.sanfoundry.com/operating-system-mcqs-multi-threading-models/",
        "https://www.sanfoundry.com/operating-system-mcqs-threads-fork-exec/",
        "https://www.sanfoundry.com/operating-system-mcqs-threads-cancellation/",
        "https://www.sanfoundry.com/operating-system-mcqs-threads-signal-handling/",
        "https://www.sanfoundry.com/operating-system-mcqs-threads-pools/",
        "https://www.sanfoundry.com/operating-system-questions-answers-virtual-memory/",
        "https://www.sanfoundry.com/operating-system-mcqs-virtual-memory-demand-paging/",
        "https://www.sanfoundry.com/operating-system-mcqs-virtual-memory-page-replacement-algorithms-1/",
        "https://www.sanfoundry.com/operating-system-mcqs-virtual-memory-page-replacement-algorithms-2/",
        "https://www.sanfoundry.com/operating-system-mcqs-virtual-memory-frame-allocation/",
        "https://www.sanfoundry.com/operating-system-mcqs-virtual-memory-thrashing/",
        "https://www.sanfoundry.com/operating-system-questions-answers-file-system-concepts/",
        "https://www.sanfoundry.com/operating-system-questions-answers-file-system-implementation/",
        "https://www.sanfoundry.com/operating-system-mcqs-file-system-interface-access-methods-1/",
        "https://www.sanfoundry.com/operating-system-mcqs-file-system-interface-access-methods-2/",
        "https://www.sanfoundry.com/operating-system-mcqs-file-system-interface-directory-structure-1/",
        "https://www.sanfoundry.com/operating-system-mcqs-file-system-interface-directory-structure-2/",
        "https://www.sanfoundry.com/operating-system-mcqs-file-system-interface-mounting-sharing/",
        "https://www.sanfoundry.com/operating-system-mcqs-file-system-interface-protection/",
        "https://www.sanfoundry.com/operating-system-mcqs-file-system-allocation-methods-1/",
        "https://www.sanfoundry.com/operating-system-mcqs-file-system-allocation-methods-2/",
        "https://www.sanfoundry.com/operating-system-mcqs-file-system-allocation-methods-3/",
        "https://www.sanfoundry.com/operating-system-mcqs-file-system-free-space-performance/",
        "https://www.sanfoundry.com/operating-system-mcqs-file-system-recovery/",
        "https://www.sanfoundry.com/operating-system-mcqs-network-file-system-1/",
        "https://www.sanfoundry.com/operating-system-mcqs-network-file-system-2/",
        "https://www.sanfoundry.com/operating-system-questions-answers-io-subsystem/",
        "https://www.sanfoundry.com/operating-system-mcqs-disk-scheduling-1/",
        "https://www.sanfoundry.com/operating-system-mcqs-disk-scheduling-2/",
        "https://www.sanfoundry.com/operating-system-mcqs-disk-management/",
        "https://www.sanfoundry.com/operating-system-mcqs-swap-space-management/",
        "https://www.sanfoundry.com/operating-system-mcqs-mass-storage-RAID-1/",
        "https://www.sanfoundry.com/operating-system-mcqs-mass-storage-RAID-2/",
        "https://www.sanfoundry.com/operating-system-mcqs-mass-storage-tertiary-storage/",
        "https://www.sanfoundry.com/operating-system-mcqs-protection-access-matrix/",
        "https://www.sanfoundry.com/operating-system-questions-answers-protection-concepts/",
        "https://www.sanfoundry.com/operating-system-questions-answers-security/",
        "https://www.sanfoundry.com/operating-system-mcqs-protection-memory-protection/",
        "https://www.sanfoundry.com/operating-system-mcqs-protection-revocation-access-rights/",
        "https://www.sanfoundry.com/operating-system-questions-answers-distributed-operating-system/",
        "https://www.sanfoundry.com/distributed-operating-system-mcqs-types-resource-sharing/",
        "https://www.sanfoundry.com/distributed-operating-system-mcqs-network-structure-topology/",
        "https://www.sanfoundry.com/distributed-operating-system-mcqs-robustness/",
        "https://www.sanfoundry.com/distributed-operating-system-mcqs-file-system-1/",
        "https://www.sanfoundry.com/distributed-operating-system-mcqs-file-system-2/",
        "https://www.sanfoundry.com/operating-system-questions-answers-distributed-file-system/",
        "https://www.sanfoundry.com/distributed-opererating-system-mcqs-coordination/",
        "https://www.sanfoundry.com/operating-system-questions-answers-distributed-synchronization/"
    ]

    def parse(self, response):
        item = CrawlerItem()
        item['QuestionAnswer'] = Selector(response).xpath(
            '//div[@class="collapseomatic_content "]/text()|//div[@class="entry-content"]/p/text()').extract()
        item['ChapterName'] = ''.join(Selector(response).xpath('//h1[@class="entry-title"]/text()').extract()[0].split('\u2013')[1:]).strip()
        item['NameId'] = '-'.join(item['ChapterName'].lower().split(' '))
        # for question in questions:
        #     item = CrawlerItem()

        #     item['User'] = question.xpath(
        #         'div[@class="rowuser"]/a/strong/text()').extract_first()
        #     item['Comment'] = question.xpath(
        #         'div[@class="question"]/text()').extract_first()
        #     item['Time'] = question.xpath(
        #         'div[@class="actionuser"]/a[@class="time"]/text()').extract_first()

        yield item
