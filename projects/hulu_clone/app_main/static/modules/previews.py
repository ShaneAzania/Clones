# global variable

from turtle import title


def previews_render(request, data):
    session = request.session
    if 'previews' in data:
        previews_html_array = [] # collect html versions of previews
        for preview in data['previews']: # an array of dictionaries
            list_items = ''
            preview_items = preview['preview_items']
            title = preview['preview_title']

            for preview_item in preview_items:
                background_img = 'static/media/'+'img/sample_4.jpeg'

                li = ''\
                    f'<li class="preview-item" style="background-image: url({background_img}); background-size: cover">'\
                        '<svg class="preview-more" viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false" >'\
                            '<circle cx="12" cy="12" r="1"></circle>'\
                            '<circle cx="12" cy="5" r="1"></circle>'\
                            '<circle cx="12" cy="19" r="1"></circle>'\
                        '</svg>'\
                        '<div class="preview-overlay">'\
                            '<svg width="48" height="48" fill="none" viewBox="0 0 48 48" class="cu-button-detail" data-testid="detail-button">'\
                                '<circle cx="24" cy="24" r="24" fill="#fff"></circle>'\
                                '<path fill-rule="evenodd" clip-rule="evenodd" d="M24.44 13.94a1.5 1.5 0 000 2.12l6.439 6.44H13.5a1.5 1.5 0 000 3h17.379l-6.44 6.44a1.5 1.5 0 002.122 2.12l9-9a1.495 1.495 0 00.325-1.634 1.497 1.497 0 00-.325-.487l-9-9a1.5 1.5 0 00-2.122 0z" fill="#040405" ></path>'\
                                '<path d="M24.44 16.06l-.177.177.176-.176zm0-2.12l-.177-.177.176.176zm6.439 8.56v.25h.603l-.427-.427-.176.177zm0 3l.176.177.427-.427h-.603v.25zm-6.44 6.44l-.176-.177.176.176zm0 2.12l-.176.177.176-.176zm2.122 0l-.177-.176.177.177zm9-9l.176.177-.176-.176zm.325-1.634l-.23.095.23-.095zm-.325-.487l.176-.176-.176.176zm-9-9l.176-.176-.176.176zm-1.945 1.945a1.25 1.25 0 010-1.768l-.353-.353a1.75 1.75 0 000 2.474l.353-.353zm6.44 6.44l-6.44-6.44-.353.353 6.439 6.44.353-.354zM13.5 22.75h17.379v-.5H13.5v.5zM12.25 24c0-.69.56-1.25 1.25-1.25v-.5A1.75 1.75 0 0011.75 24h.5zm1.25 1.25c-.69 0-1.25-.56-1.25-1.25h-.5c0 .966.784 1.75 1.75 1.75v-.5zm17.379 0H13.5v.5h17.379v-.5zm-6.263 6.866l6.44-6.44-.354-.353-6.44 6.44.354.353zm0 1.768a1.25 1.25 0 010-1.768l-.353-.353a1.75 1.75 0 000 2.474l.353-.353zm1.768 0a1.25 1.25 0 01-1.768 0l-.353.353a1.75 1.75 0 002.474 0l-.353-.353zm9-9l-9 9 .353.353 9-9-.353-.353zM35.75 24c0 .32-.122.64-.366.884l.353.353c.342-.341.513-.79.513-1.237h-.5zm-.095-.478c.061.147.095.308.095.478h.5c0-.237-.047-.463-.133-.67l-.462.192zm-.271-.406c.12.12.21.258.271.405l.462-.19a1.745 1.745 0 00-.38-.568l-.353.353zm-9-9l9 9 .353-.353-9-9-.353.353zm-1.768 0a1.25 1.25 0 011.768 0l.353-.353a1.75 1.75 0 00-2.474 0l.353.353z" fill="#fff"></path>'\
                            '</svg>'\
                        '</div>'\
                    '</li>'

                list_items += li

            this_previews = ''\
                '<div class="previews container-fluid">'\
                    f'<h5 class="previews-title">{title}</h5>'\
                    '<div class="preview-slider">'\
                        '<ul>'\
                            f'{list_items}'\
                        '</ul>'\
                    '</div>'\
                '</div>'
            previews_html_array.append(this_previews)
    
    return previews_html_array